# -*- coding: utf-8 -*-
from PyQt5.QtCore import (QSettings, QTranslator, qVersion, QCoreApplication,
                          QObject, QThread, pyqtRemoveInputHook, pyqtSignal,
                          QVariant)
from PyQt5.QtGui import QIcon, QDoubleValidator, QColor
from PyQt5.QtWidgets import QAction

from qgis.core import *
from qgis.gui import *

import os.path
import processing
from osgeo import ogr, osr
from math import isnan

import time

MESSAGE_CATEGORY = 'AwaP'

class AwaPWorker(QgsTask):
    """This shows how to subclass QgsTask"""

    # layerPrint = pyqtSignal('QgsMapLayerType', str, str, dict)
    layerPrint = pyqtSignal(QgsVectorLayer,  dict)
    layerPrintStyled = pyqtSignal(QgsVectorLayer, str)
    # logSignal = pyqtSignal(str)


    def __init__(self, parent, description):
        super().__init__(description, QgsTask.CanCancel)
        self.exception = None
        self.parent = parent
    
    def log(self, message: str, level=Qgis.Info):
        QgsMessageLog.logMessage(message, MESSAGE_CATEGORY, level=level)

    def run(self):
        """Here you implement your heavy lifting.
        Should periodically test for isCanceled() to gracefully
        abort.
        This method MUST return True or False.
        Raising exceptions will crash QGIS, so we handle them
        internally and raise them in self.finished
        """
        starttime = time.time()

        self.log('Started task "%s"' %self.description())

        # Note if the layers will be styled with a custom color map or not
        # This will determine the function in the main thread where the
        # resulting layers will be returned
        self.styleResultingLayers = self.parent.dlg.checkBox_6.isChecked()

        # Does the user want to color layers by Area, Perimeter or AwaP?
        # [3:] removes the characters 'by ' from the string
        self.colorby = self.parent.dlg.comboBox.currentText()[3:]

        # Note if the custom coloring option is set to by AwaP because in
        # this case the resulting layer will contain grid cells instead of
        # blocks
        self.colorByAwap =  self.parent.dlg.checkBox_6.isChecked() and \
            self.parent.dlg.comboBox.currentIndex() == 2

        # THIS IS WHERE I GET THE PARAMETERS FROM THE PLUGIN DIALOG
        self.blocks_layer = self.parent.dlg.mMapLayerComboBox.currentLayer()
        # self.log('blocks_layer = %s' %self.blocks_layer.sourceName())

        self.boundary_option_single = self.parent.dlg.radioButton.isChecked()
        # if self.boundary_option_single:
        #     # self.log('calculate single AwaP for the entire boundary layer')
        self.boundary_option_multiple = self.parent.dlg.radioButton_2.isChecked()
        # if self.boundary_option_multiple:
            # self.log('calculate separate AwaP for each polygon in the boundary layer')

        self.boundary_layer = self.parent.dlg.mMapLayerComboBox_2.currentLayer()
        # self.log('boundary_layer = %s' %self.boundary_layer.sourceName())

        self.deadend_solution = self.parent.dlg.checkBox_3.checkState()
        # self.log('deadend solution enabled: %s' %self.deadend_solution)

        self.buffering_distance = self.parent.dlg.mQgsDoubleSpinBox.value()/2
        # if self.deadend_solution:
            # self.log('buffering distance: %s' %self.buffering_distance)

        self.always_in = self.parent.dlg.checkBox.checkState()
        self.always_out = self.parent.dlg.checkBox_2.checkState()
        self.percent_in = self.parent.dlg.mQgsSpinBox.value()

        self.project_crs = self.parent.iface.mapCanvas().mapSettings().destinationCrs().authid()
        if self.project_crs == '':
            self.project_crs = '3857'
        # self.log('The plugin is working on the project CRS: %s' %self.project_crs)

        if self.isCanceled():
            return False

        # Preliminary fix the blocks layer
        self.blocks_layer = processing.run(
            'qgis:fixgeometries',
            {
                'INPUT': self.blocks_layer,
                'OUTPUT': 'memory:',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        # REPROJECT both boundary and sp layers
        self.blocks_layer = processing.run(
            'qgis:reprojectlayer',
            {
                'INPUT': self.blocks_layer,
                'TARGET_CRS': self.project_crs,
                'OUTPUT': 'memory:',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        self.boundary_layer = processing.run(
            'qgis:reprojectlayer',
            {
                'INPUT': self.boundary_layer,
                'TARGET_CRS': self.project_crs,
                'OUTPUT': 'memory:boundary',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        # first check if the boundary layer == lines
        if self.boundary_layer.geometryType() == 1:
            self.boundary_layer = processing.run(
                'qgis:linestopolygons',
                {
                    'INPUT': self.boundary_layer,
                    'OUTPUT': 'memory:boundary',
                }
            )['OUTPUT']

        if self.isCanceled():
            return False

        # Preliminary fix the boundary layer
        self.boundary_layer = processing.run(
            'qgis:fixgeometries',
            {
                'INPUT': self.boundary_layer,
                'OUTPUT': 'memory:',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        # this is where I need to select from the blocks layer only those features which intersect with the boundary
        self.blocks_layer = processing.run(
            'qgis:extractbylocation',
            {
                'INPUT' : self.blocks_layer,
                'PREDICATE' : [0],
                'INTERSECT' : self.boundary_layer,
                'OUTPUT' : 'memory:',
            }
        )['OUTPUT']

###################################################################
####### HANDLING THE BLOCKS LAYER

        if self.isCanceled():
            return False

        # check if the blocks layer == lines
        if self.blocks_layer.geometryType() == 1:
            self.blocks_layer = processing.run(
                'qgis:linestopolygons',
                {
                    'INPUT': self.blocks_layer,
                    'OUTPUT': 'memory:',
                }
            )['OUTPUT']

        # dissolve the created polygons in order to make touching polyigons
        # into one block
        pathdissolve = processing.run(
            'qgis:dissolve',
            {
                'INPUT':self.blocks_layer,
                'OUTPUT': 'memory:dissolve',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        # convert dissolve result from multipart to singleparts
        self.blocks_layer = processing.run(
            'qgis:multiparttosingleparts',
            {
                'INPUT': pathdissolve,
                'OUTPUT': 'memory:singleparts',
            }
        )['OUTPUT']

        if self.isCanceled():
            return False

        # see if the deadend solution has been selected when the plugin was run
        # if true, run the whole buffering solution for removing deadends from
        # the results
        if self.deadend_solution:
            # first I need to buffer out the blocks by the given distance
            # amount
            buffer_out_layer = processing.run(
                'qgis:buffer',
                {
                    'INPUT' : self.blocks_layer,
                    'END_CAP_STYLE' : 1,
                    'OUTPUT' : 'memory:bufferout',
                    'SEGMENTS' : 90,
                    'DISTANCE' : self.buffering_distance,
                    'JOIN_STYLE' : 0,
                    'MITER_LIMIT': 2,
                    'DISSOLVE' : False,
                }
            )['OUTPUT']

            if self.isCanceled():
                return False

            # then I need to buffer back in by the same distance amount
            buffer_in_layer = processing.run(
                'qgis:buffer',
                {
                    'INPUT' : buffer_out_layer,
                    'END_CAP_STYLE' : 1,
                    'OUTPUT' : 'memory:bufferin',
                    'SEGMENTS' : 90,
                    'DISTANCE' : -self.buffering_distance,
                    'JOIN_STYLE' : 0,
                    'MITER_LIMIT': 2,
                    'DISSOLVE' : False,
                }
            )['OUTPUT']

            self.blocks_layer = buffer_in_layer

        if self.isCanceled():
            return False

        # finally, fill in any wholes that are left in the blocks
        self.blocks_layer = processing.run(
            'qgis:deleteholes',
            {
                'INPUT' : self.blocks_layer,
                'MIN_AREA' : 0,
                'OUTPUT' : 'memory:deleteholes',
            }
        )['OUTPUT']

        def calculateAwaP(self, boundary_geom):
            """This is a function for a single run of the AwaP calculation"""

            self.final_blocks_layer =  QgsVectorLayer('Polygon?crs='+self.project_crs, 'IC_blocks' , "memory")

            # get the data provider of the blocks layer
            provider = self.final_blocks_layer.dataProvider()

            # Create attribute fields to hold area, and perimeter values
            provider.addAttributes(
                [
                    QgsField('awap_id', QVariant.Int),
                    QgsField('Area', QVariant.Double),
                    QgsField('Perimeter', QVariant.Double),
                    QgsField('AwaP', QVariant.Double)
                ]
            )

            # Tell vector layer to update fields in order to get the new layers
            # from data provider
            self.final_blocks_layer.updateFields()

            # AwaP is calculated as sum(Perimeter x Area) / sum(Area)
            # keep track of both numerator and denominator of this equation
            numerator_sumPxA = 0
            denominator_sumA = 0

            # Now I need to fetch column numbers of these new attributes for when
            # I need to update them later on
            awap_id_id = provider.fieldNameIndex('awap_id')
            area_id = provider.fieldNameIndex('Area')
            perimeter_id = provider.fieldNameIndex('Perimeter')

            i = 1

            if self.always_in:
                # for boundary in self.boundary_layer.getFeatures():
                #     boundary_geom = boundary.geometry()

                with edit(self.final_blocks_layer):
                    for block in self.blocks_layer.getFeatures():
                        if self.isCanceled():
                            return False
                        block_geom = block.geometry()

                        if block_geom.intersects(boundary_geom):

                            # Calculate area and perimeter of the block
                            P = block_geom.length()
                            A = block_geom.area()

                            # Create a new feature with the geometry of the
                            # block and the id, perimeter and area attributes
                            feature = QgsFeature()
                            feature.setGeometry(block_geom)
                            feature.setId(i)
                            provider.addFeatures( [feature] )

                            # Add area and perimeter of the block to the attribute
                            # table
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                awap_id_id,
                                i
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                area_id,
                                A
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                perimeter_id,
                                P
                            )

                            # Finally, keep incrementing (summing) num & denum
                            numerator_sumPxA += P * A
                            denominator_sumA += A
                            #  print("Area:", block_geom.area())

                            i += 1

            elif self.always_out:
                # for boundary in self.boundary_layer.getFeatures():
                #     boundary_geom = boundary.geometry()

                with edit(self.final_blocks_layer):
                    for block in self.blocks_layer.getFeatures():
                        if self.isCanceled():
                            return False
                        block_geom = block.geometry()

                        if block_geom.within(boundary_geom):
                            P = block_geom.length()
                            A = block_geom.area()

                            # Create a new feature with the geometry of the
                            # block and the id, perimeter and area attributes
                            feature = QgsFeature()
                            feature.setGeometry(block_geom)
                            feature.setId(i)
                            provider.addFeatures( [feature] )

                            # Add area and perimtere of the block to the attribute
                            # table
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                awap_id_id,
                                i
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                area_id,
                                A
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                perimeter_id,
                                P
                            )

                            # Finally, keep incrementing (summing) num & denum
                            numerator_sumPxA += P * A
                            denominator_sumA += A
                            #  print("Area:", block_geom.area())

                            i += 1

            else:
                # for boundary in self.boundary_layer.getFeatures():
                #     boundary_geom = boundary.geometry()

                with edit(self.final_blocks_layer):
                    for block in self.blocks_layer.getFeatures():
                        if self.isCanceled():
                            return False
                        block_geom = block.geometry()

                        block_intersection = block_geom.intersection(boundary_geom)

                        A = block_geom.area()
                        if A > 0:
                            block_percent = block_intersection.area() / A * 100
                            #  print('block_percent: ', block_percent)
                            #  print('percent_in: ', self.percent_in)
                        else:
                            block_percent = 0

                        if block_percent >= self.percent_in:
                            P = block_geom.length()

                            # Create a new feature with the geometry of the
                            # block and the id, perimeter and area attributes
                            feature = QgsFeature()
                            feature.setGeometry(block_geom)
                            feature.setId(i)
                            provider.addFeatures( [feature] )

                            # Add area and perimtere of the block to the attribute
                            # table
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                awap_id_id,
                                i
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                area_id,
                                A
                            )
                            self.final_blocks_layer.changeAttributeValue(
                                i,
                                perimeter_id,
                                P
                            )

                            # Finally, keep incrementing (summing) num & denum
                            numerator_sumPxA += P * A
                            denominator_sumA += A
                            # print("Area:", block_geom.area())

                            i += 1

            if denominator_sumA:
                # todo round 2
                AwaP = numerator_sumPxA / denominator_sumA
            else:
                AwaP = 0
            #  print('AwaP: ', AwaP)

            # Put the calculated AwaP into the label that shows the result
            # self.parent.dlg.label_6.setText('%s m' %round(AwaP,1))
            # self.parent.dlg.label_7.setVisible(True)
            # self.parent.dlg.label_6.setVisible(True)

            # show the blocks layer in the qgis map
            awap_id = provider.fieldNameIndex('AwaP')
            with edit(self.final_blocks_layer):
                for block in self.blocks_layer.getFeatures():
                    if self.isCanceled():
                            return False
                    self.final_blocks_layer.changeAttributeValue(
                        block.id(),
                        awap_id,
                        AwaP
                    )
            self.final_blocks_layer.updateFields()
            self.final_blocks_layer.setName('AwaP_' + str(int(round(AwaP,0))))

            res = {
                'AwaP result blocks layer' : self.final_blocks_layer,
                'AwaP' : AwaP,
            }

            return res


        if self.boundary_option_single:
            self.boundary_layer = processing.run(
                'qgis:dissolve',
                {
                    'INPUT': self.boundary_layer,
                    'OUTPUT': 'memory:boundary_dissolved',
                }
            )['OUTPUT']

        if self.colorByAwap is False:
            # this is the default operation when coloring by perimeter or area
            # and blocks need to be produced for each boundary and saved for
            # visualisation
            self.resulting_layers = []
            for boundary in self.boundary_layer.getFeatures():
                boundary_geom = boundary.geometry()
                result = calculateAwaP(self, boundary_geom).get('AwaP result blocks layer')
                if result is False:
                    return False
                else:
                    self.resulting_layers.append(result)
        elif self.colorByAwap is True:
            # this is when the multible boundaries are in use and the results
            # only need to show grid cells colored by AwaP, blocks are not
            # returned in this option

            # first add the attribute field AwaP in the boundary layer - this will hold
            # AwaP results for each grid cell
            provider = self.boundary_layer.dataProvider()
            provider.addAttributes(
                [
                    QgsField('AwaP', QVariant.Double)
                ]
            )
            awap_id = provider.fieldNameIndex('AwaP')
            # now iterate through each grid cell and assign resulting AwaP
            with edit(self.boundary_layer):
                for boundary in self.boundary_layer.getFeatures():
                    boundary_geom = boundary.geometry()
                    result = calculateAwaP(self, boundary_geom)
                    if result is False:
                        return False
                    else:
                        self.boundary_layer.changeAttributeValue(
                            boundary.id(),
                            awap_id,
                            result.get('AwaP')
                        )

            # use self.resulting_layers to store the boundary layer for showing on the map
            # because this is already handled in the finished() method, avoids extra code
            self.boundary_layer.setName('AwaP cells')
            self.resulting_layers = [self.boundary_layer]
        
        endtime = time.time()
        self.duration = endtime-starttime

        return True

    def finished(self, result):
        """
        This function is automatically called when the task has
        completed (successfully or not).
        You implement finished() to do whatever follow-up stuff
        should happen after the task is complete.
        finished is always called from the main thread, so it's safe
        to do GUI operations and raise Python exceptions here.
        result is the return value from self.run.
        """
        if result:
            self.log(
                'Task "{name}" completed in {duration} s'.format(
                  name=self.description(),
                  duration=self.duration
                ),
              Qgis.Success)
            
            for layer in self.resulting_layers:
                if self.styleResultingLayers:
                    self.layerPrintStyled.emit(layer, self.colorby)
                else:
                    self.layerPrint.emit(
                        layer,
                        {'color' : QColor(128, 55, 55).rgb()}
                    )

        else:
            if self.exception is None:
                self.log(
                    'Task "{name}" not successful but without '\
                    'exception (probably the task was manually '\
                    'canceled by the user)'.format(
                        name=self.description()),
                    Qgis.Warning)

            else:
                self.log(
                    'Task "{name}" Exception: {exception}'.format(
                        name=self.description(),
                        exception=self.exception),
                    Qgis.Critical)
                raise self.exception

    def cancel(self):
        self.log(
            'Task "{name}" was canceled'.format(
                name=self.description()),
            Qgis.Info)
        super().cancel()