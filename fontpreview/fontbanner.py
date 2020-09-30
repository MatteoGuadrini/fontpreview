#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# fontbanner -- fontpreview
#
#     Copyright (C) 2020 Matteo Guadrini <matteo.guadrini@hotmail.it>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .fontpreview import FontPreview, CALC_POSITION


class FontBanner(FontPreview):
    """
    Class that represents the banner of a font
    """

    def __init__(self, font, orientation='landscape', bg_color='white', fg_color='black', mode='letter'):
        """
        Object that represents the banner of a font
        :param font: font file
        :param orientation: the orientation of the banner; 'landscape', 'portrait' or tuple(x,y)
        :param bg_color: background color
        :param fg_color: font color
        :param mode: the text inside the banner; 'letter','fontname', 'paragraph', 'alpha' and 'combination'
        """
        # Define properties
        FontPreview.__init__(self, font=font)
        self.set_orientation(orientation)
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.mode = mode
        self.font_position = CALC_POSITION['center'](self.dimension, self.font.getsize(self.font_text))
        # Create default image
        self.draw()

    def set_orientation(self, orientation):
        """
        Set orientation of banner
        :param orientation: the orientation of the banner; 'landscape' or 'portrait'
        :return: None
        """
        LANDSCAPE = (1653, 560)
        PORTRAIT = (560, 1653)
        # Calculate banner size
        if isinstance(orientation, tuple):
            self.dimension = orientation
            return None
        if orientation == 'landscape':
            self.dimension = LANDSCAPE
        elif orientation == 'portrait':
            self.dimension = PORTRAIT
        else:
            raise ValueError('orientation is "landscape","portrait" or tuple(x,y)')