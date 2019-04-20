title: Python Code To Generate Full Size Yearly Calendar in Inkscape
slug: python-calendar-app
meta: An article about the Python code which generates full size yearly calendar. 
date: 2019-04-12 14:06
modified: 2019-04-12 14:06
tags: python, inkscape
note: add a github link


At-A-Glance DayMinder Monthly Planner 7" x 8-3/4" Version had been my calendar 
for a few years.  Then I found the excellent PDF software 
[PDFXChange-Viewer]({filename}/posts/pdfxchange-viewer.md) 
and I started downloading monthly PDF calendars from 
[timeanddate.com](https://www.timeanddate.com/calendar/create.html). 
Each file was for one year, it had 13 pages.  The first page was a yearly 
calendar and other 12 pages were monthly calendars.  I marked events on the PDF 
directly with 10 point "Narrow Arial" fonts. This continued for 
a few years. 

After I became familiar with Inkscape extension and Python programming, I 
wrote a python program which generates full size (36" x 24") one page yearly calendar
in Inkscape. I save both SVG and PDF files. 

Now the one page PDF file is my daily calendar, and I mark events on the PDF. 
My event descriptions are usually very short like "9am meeting with Don", 
"10:45 See Dr Jeff", and "off work vacation in FL" 

Here is what the yearly calendar looks like. 

<div style="max-width:800px">
  <img class="img-fluid" src="/images/img-calendar-2019.svg" alt="calendar example"> 
</div>

Here are the links for calendars from 2019 to 2025.  I will add more links to this page 
in year 2025.

* 2019: [svg](/files/calendar/2019.svg) [pdf](/files/calendar/2019.pdf)
* 2020: [svg](/files/calendar/2020.svg) [pdf](/files/calendar/2020.pdf)
* 2021: [svg](/files/calendar/2021.svg) [pdf](/files/calendar/2021.pdf)
* 2022: [svg](/files/calendar/2022.svg) [pdf](/files/calendar/2022.pdf)
* 2023: [svg](/files/calendar/2023.svg) [pdf](/files/calendar/2023.pdf)
* 2024: [svg](/files/calendar/2024.svg) [pdf](/files/calendar/2024.pdf)
* 2025: [svg](/files/calendar/2025.svg) [pdf](/files/calendar/2025.pdf)

Here are the code in create_calendar.inx and create_calendar.py files. 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension xmlns="http://www.inkscape.org/namespace/inkscape/extension">
  <_name>Create Calendar</_name>
  <id>create_calendar.com.gotrafficsign</id>
  <dependency type="executable" location="extensions">inkex.py</dependency>
  <dependency type="executable" location="extensions">simplestyle.py</dependency>
  <param name="yearNumber" type="int" min="0" max="2100" gui-text="For Year: ">2019</param>

  <effect>
    <object-type>all</object-type>
    <effects-menu>
      <submenu _name="OpenCalendar">
      </submenu>
    </effects-menu>
  </effect>

  <script>
    <command reldir="extensions" interpreter="python">create_calendar.py</command>
  </script>

</inkscape-extension>

```

```python
#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
# create_calendar.py
Create post size calendar file in Inkscape

Copyright (C) December 08 2018 George Zhang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import inkex
import simplestyle
import simpletransform
import sys
import math
import copy
import os
import re
import datetime
import calendar
import logging

class CreateCalendar(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option(
            "--yearNumber", action="store", type="int", dest="yearN", default="1")

        logging.basicConfig(level=logging.DEBUG, filename="logging.txt")

    def effect(self):
        PAGE_W = 36
        PAGE_H = 24

        w = PAGE_W
        h = PAGE_H

        self.change_SVG_size(w, h)

        year = self.options.yearN
        month = 1
        width = 9
        height = 8

        i = j = 0
        for month in range(1, 13):
            i = (month-1) % 4
            j = (month-1) / 4 # python 2 only
            x = i * 9
            y = j * 8
            self.draw_month(year, month, width, height, x, y)

    def change_SVG_size(self, width, height):
        ratio = 25.4
        svg_elem = self.document.getroot()

        page_width = width
        page_height = height

        svg_elem.set('width', str(page_width) + 'in')
        svg_elem.set('height', str(page_height) + 'in')
        svg_elem.set('viewBox', '0 0 ' + str(page_width * ratio) + ' '
                     + str(page_height * ratio))

    def draw_SVG_line(self, (x1, y1), (x2, y2), style, name, parent):
        '''style is a dict'''
        line_attribs = {'style': simplestyle.formatStyle(style),
                        inkex.addNS('label', 'inkscape'): name,
                        'd': 'M ' + str(x1) + ',' + str(y1) + ' L' +
                        str(x2) + ',' + str(y2)}
        elm = inkex.etree.SubElement(
            parent, inkex.addNS('path', 'svg'), line_attribs)
        return elm

    def draw_lines(self, layer, width, height):
        line_style = {'stroke': '#000000',
                      'stroke-width': str(self.unittouu('1px')),
                      'fill': 'none'}

        for i in range(1, 4):
            x1_str = str(9 * i) + 'in'
            y1_str = '0.25in'
            y2_str = str(height - 0.25) + 'in'
            x1, x2, y1, y2 = map(
                self.unittouu, [x1_str, x1_str, y1_str, y2_str])
            self.draw_SVG_line((x1, y1), (x2, y2), line_style, 'line', layer)

        for j in range(1, 3):
            x1_str = '0.25in'
            x2_str = str(width - 0.25) + 'in'
            y1_str = str(8 * j) + 'in'
            x1, x2, y1, y2 = map(
                self.unittouu, [x1_str, x2_str, y1_str, y1_str])
            self.draw_SVG_line((x1, y1), (x2, y2), line_style, 'line', layer)

    def draw_grid(self, layer, width, height, num_col, num_row, x, y):
        '''width and height, in in inches, same for x and y'''
        line_style = {'stroke': '#000000',
                      'stroke-width': str(self.unittouu('1px')),
                      'fill': 'none'}

        for i in range(num_col + 1):
            x1_str = str(x + (float(width)/num_col) * i) + 'in'
            x2_str = x1_str
            y1_str = str(y) + 'in'
            y2_str = str(y + height) + 'in'
            x1, x2, y1, y2 = map(
                self.unittouu, [x1_str, x2_str, y1_str, y2_str])
            self.draw_SVG_line((x1, y1), (x2, y2), line_style, 'line', layer)

        for i in range(num_row + 1):
            x1_str = str(x) + 'in'
            x2_str = str(x + width) + 'in'
            y1_str = str(y + (float(height)/num_row) * i) + 'in'
            y2_str = y1_str
            x1, x2, y1, y2 = map(
                self.unittouu, [x1_str, x2_str, y1_str, y2_str])
            logging.debug("%s %s %s %s" % (x1_str, x2_str, y1_str, y2_str))
            logging.debug("%s %s %s %s" % (x1, x2, y1, y2))
            self.draw_SVG_line((x1, y1), (x2, y2), line_style, 'line', layer)

    def draw_month(self, year, month, width, height, x, y):
        '''height and width in inches int
        x and y in inches from top left corner'''
        # num_col = 7
        # num_row = 5
        cal = calendar.Calendar(6) # set Sunday as first day

        width = width - 0.4
        height = height - 0.4
        x = x + 0.2
        y = y + 0.2

        # assert num_row in (4, 5, 6), "num of row should be 4 5 or 6"
        # width_col = float(width) / num_col
        # height_row = float(height) / num_row

        x_month = x + float(width) / 2
        y_month = y
        ratio = 25.4
        x_month_R, y_month_R = (x_month * ratio, y_month * ratio)

        y_month_R += 9.15 + 7 # 7 from observation
        text_layer = self.find_create_layer(self.document.getroot(),
            'text_layer')
        elem = self.draw_month_text(x_month_R, y_month_R, month, year)
        text_layer.append(elem)

        x_dayofweek = x + float(width) / 7.0 / 2
        y_dayofweek = y + 1.35
        x_dayofweek_R, y_dayofweek_R = (x_dayofweek * ratio,
            y_dayofweek * ratio)

        for i in range(7):
            elem = self.draw_weekday_text(x_dayofweek_R, y_dayofweek_R, i)
            text_layer.append(elem)
            x_dayofweek_R += float(width) / 7.0 * ratio

        bk_layer = self.find_create_layer(self.document.getroot(), 'bk_layer')

        num_col = 7
        num_row = len(cal.monthdayscalendar(year, month))

        self.draw_grid(bk_layer, width, height - 1.5, num_col, num_row,
            x, y+1.5)

        cal_matrix = cal.monthdayscalendar(year, month)

        for i in range(num_row):
            for j in range(num_col):
                day_num = cal_matrix[i][j]
                if day_num != 0:
                    self.draw_text(text_layer, width, height - 1.5,
                        num_col, num_row, x, y+1.5, str(day_num), j, i)

    def draw_text(self, layer, width, height, num_col, num_row, x, y,
        name, i, j):
        '''place day number in a monthly grid'''

        x_loc = x + (float(width)/num_col) * i
        y_loc = y + (float(height)/num_row) * j # top left corner

        ratio = 25.4

        x_loc_R = x_loc * ratio
        y_loc_R = y_loc * ratio

        y_loc_R += 6.097  # vertical adjustement, vertical align baseline

        x_loc_R += 2
        y_loc_R += 2  # second adjustment

        elem = self.create_text(x_loc_R, y_loc_R, name)
        layer.append(elem)

    def create_text(self, x, y, name):

        style_d = {'font-size': '6.34px',  # 18 pt
                   'font-family': 'Roboto',
                   #   'text-align': 'center',
                   'text-anchor': 'start',
                   'fill': '#000000',
                   'stroke': 'none',
                   }
        t = inkex.etree.Element('text')
        t.set(inkex.addNS('space', 'xml'), 'preserve')
        t.set('x', str(x))
        t.set('y', str(y))
        t.set('style', simplestyle.formatStyle(style_d))

        sp = inkex.etree.SubElement(t, 'tspan')
        sp.set(inkex.addNS('role', 'sodipodi'), 'line')
        sp.text = name
        return t

    def draw_month_text(self, x, y, month, year):
        month_name_str = ['0', 'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December']

        style_d = {'font-size': '12.69px',  # 24 pt
                   'font-family': 'Roboto',
                   #'text-align': 'center',
                   'text-anchor': 'middle',
                   'fill': '#000000',
                   'stroke': 'none',
                   }
        t = inkex.etree.Element('text')
        t.set(inkex.addNS('space', 'xml'), 'preserve')
        t.set('x', str(x))
        t.set('y', str(y))
        t.set('style', simplestyle.formatStyle(style_d))

        sp = inkex.etree.SubElement(t, 'tspan')
        sp.set(inkex.addNS('role', 'sodipodi'), 'line')
        sp.text = month_name_str[month] + ' ' + str(year)
        return t

    def draw_weekday_text(self, x, y, dayofweek):
        dayofweek_str = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday' ]

        style_d = {'font-size': '8.46px',  # 24 pt
                   'font-family': 'Roboto',
                   #'text-align': 'center',
                   'text-anchor': 'middle',
                   'fill': '#000000',
                   'stroke': 'none',
                   }
        t = inkex.etree.Element('text')
        t.set(inkex.addNS('space', 'xml'), 'preserve')
        t.set('x', str(x))
        t.set('y', str(y))
        t.set('style', simplestyle.formatStyle(style_d))

        sp = inkex.etree.SubElement(t, 'tspan')
        sp.set(inkex.addNS('role', 'sodipodi'), 'line')
        sp.text = dayofweek_str[dayofweek][0:3]
        return t

    def find_create_layer(self, parent, layer_name):
        # this should not be svg:g
        path = '//g[@inkscape:label="%s"]' % layer_name
        path += '|//svg:g[@inkscape:label="%s"]' % layer_name
        el_list = self.document.xpath(path, namespaces=inkex.NSS)
        # inkex.debug(el_list)
        if el_list:
            layer = el_list[0]
            #inkex.debug('this code never execute, why?')
        else:
            layer = inkex.etree.SubElement(parent, 'g')
            layer.set(inkex.addNS('label', 'inkscape'), layer_name)
            layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
        return layer

    def create_group(self, group_name):
        group = inkex.etree.Element('g')
        group.set(inkex.addNS('label', 'inkscape'), group_name)
        group.set('fill', 'none')
        return group
        
if __name__ == '__main__':
    e = CreateCalendar()
    e.affect()

```