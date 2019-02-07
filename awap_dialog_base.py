<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AwaPDialogBase</class>
 <widget class="QDialog" name="AwaPDialogBase">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>404</width>
    <height>394</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>AwaP</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QScrollArea" name="scrollArea">
     <property name="widgetResizable">
      <bool>true</bool>
     </property>
     <widget class="QWidget" name="scrollAreaWidgetContents">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>384</width>
        <height>374</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout">
         <item>
          <widget class="QLabel" name="label">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;blocks&lt;/span&gt; for which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;blocks&lt;/span&gt; for which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>Blocks layer:</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QgsMapLayerComboBox" name="mMapLayerComboBox">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;blocks&lt;/span&gt; for which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;blocks&lt;/span&gt; for which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_2">
         <item>
          <widget class="QLabel" name="label_2">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;boundary&lt;/span&gt; of the area in which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;boundary&lt;/span&gt; of the area in which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>Boundary layer:</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QgsMapLayerComboBox" name="mMapLayerComboBox_2">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;boundary&lt;/span&gt; of the area in which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Please select a &lt;span style=&quot; font-weight:600;&quot;&gt;vector layer&lt;/span&gt; (lines or polygons) containing &lt;span style=&quot; font-weight:600;&quot;&gt;boundary&lt;/span&gt; of the area in which you wish to calculate &lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;AwaP&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <widget class="QLabel" name="label_3">
         <property name="toolTip">
          <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
         </property>
         <property name="whatsThis">
          <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
         </property>
         <property name="text">
          <string>Blocks intersecting boundary:</string>
         </property>
        </widget>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_5">
         <item>
          <widget class="QCheckBox" name="checkBox_4">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>include if at least</string>
           </property>
           <property name="tristate">
            <bool>false</bool>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QgsSpinBox" name="mQgsSpinBox">
           <property name="minimumSize">
            <size>
             <width>60</width>
             <height>23</height>
            </size>
           </property>
           <property name="maximumSize">
            <size>
             <width>100</width>
             <height>16777215</height>
            </size>
           </property>
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="suffix">
            <string>%</string>
           </property>
           <property name="value">
            <number>50</number>
           </property>
           <property name="showClearButton">
            <bool>false</bool>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLabel" name="label_5">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>of block area is inside.</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer_3">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_3">
         <item>
          <widget class="QCheckBox" name="checkBox">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="layoutDirection">
            <enum>Qt::LeftToRight</enum>
           </property>
           <property name="text">
            <string>always include</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_4">
         <item>
          <widget class="QCheckBox" name="checkBox_2">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Edge block inclusion:&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always in&lt;/span&gt; - blocks that are partially inside the selected boundary are always included in the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;Always out&lt;/span&gt; - blocks that are partially inside the selected boundary are always excluded from the AwaP calculation.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600; text-decoration: underline;&quot;&gt;In if at least x% of the block is in&lt;/span&gt; - out of blocks that are partially inside the selected boundary, only the blocks with at least (&amp;gt;=) x% of their area inside the boundary are included in the AwaP calculation.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="layoutDirection">
            <enum>Qt::LeftToRight</enum>
           </property>
           <property name="text">
            <string>always exclude</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer_2">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_7">
         <item>
          <widget class="QLabel" name="label_4">
           <property name="text">
            <string>Dead-end removal:</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer_5">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_8">
         <item>
          <widget class="QCheckBox" name="checkBox_3">
           <property name="layoutDirection">
            <enum>Qt::LeftToRight</enum>
           </property>
           <property name="text">
            <string>yes, max. street width</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QgsDoubleSpinBox" name="mQgsDoubleSpinBox">
           <property name="maximum">
            <double>1000000.000000000000000</double>
           </property>
           <property name="singleStep">
            <double>0.500000000000000</double>
           </property>
           <property name="value">
            <double>40.000000000000000</double>
           </property>
           <property name="clearValue">
            <bool>false</bool>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer_6">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_9">
         <item>
          <widget class="QCheckBox" name="checkBox_5">
           <property name="text">
            <string>no</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <spacer name="verticalSpacer">
         <property name="orientation">
          <enum>Qt::Vertical</enum>
         </property>
         <property name="sizeHint" stdset="0">
          <size>
           <width>20</width>
           <height>40</height>
          </size>
         </property>
        </spacer>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_6">
         <item>
          <widget class="QLabel" name="label_7">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;AwaP = sum(Area * Perimeter) / sum(Area)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;AwaP = sum(Area * Perimeter) / sum(Area)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt; font-weight:600;&quot;&gt;AwaP = &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLabel" name="label_6">
           <property name="toolTip">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;AwaP = sum(Area * Perimeter) / sum(Area)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="whatsThis">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;AwaP = sum(Area * Perimeter) / sum(Area)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
           <property name="text">
            <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;value&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer_4">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <spacer name="verticalSpacer_2">
         <property name="orientation">
          <enum>Qt::Vertical</enum>
         </property>
         <property name="sizeHint" stdset="0">
          <size>
           <width>20</width>
           <height>40</height>
          </size>
         </property>
        </spacer>
       </item>
       <item>
        <widget class="QDialogButtonBox" name="button_box">
         <property name="orientation">
          <enum>Qt::Horizontal</enum>
         </property>
         <property name="standardButtons">
          <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </widget>
   </item>
  </layout>
 </widget>
 <customwidgets>
  <customwidget>
   <class>QgsDoubleSpinBox</class>
   <extends>QDoubleSpinBox</extends>
   <header>qgsdoublespinbox.h</header>
  </customwidget>
  <customwidget>
   <class>QgsMapLayerComboBox</class>
   <extends>QComboBox</extends>
   <header>qgsmaplayercombobox.h</header>
  </customwidget>
  <customwidget>
   <class>QgsSpinBox</class>
   <extends>QSpinBox</extends>
   <header>qgsspinbox.h</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
