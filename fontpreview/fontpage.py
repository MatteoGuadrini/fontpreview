#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# fontpage -- fontpreview
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

# region imports
from .fontpreview import FontPreview, CALC_POSITION
from .fontbanner import FontBanner, FontLogo, resize
from PIL import Image


# endregion

# region classes
class FontPage:
    """
    Class that represents the page of a font banners
    """

    def __init__(self, template=None, dimension=(2480, 3508)):
        """
        Object that represents the page of a font banners
        :param template: template used to build the page
        :param dimension: dimension of page. Default A4 in pixels.
        """
        self.logo = None
        self.header = None
        self.body = None
        self.footer = None
        self.template = template
        self.dimension = dimension
        self.color_system = 'RGB'
        self.page = Image.new(self.color_system, self.dimension, color='white')

    def set_header(self, header):
        """
        Set header of Font page
        :param header: FontPreview object
        :return: None
        """
        # Check if header is FontPreview object
        if isinstance(header, FontPreview):
            # Check width of header
            if self.page.width != header.image.width:
                header.dimension = (self.page.width, header.image.height)
                header.font_position = CALC_POSITION['center'](header.dimension, header.font.getsize(header.font_text))
            self.header = header
            # Check height of header
            if header.image.height > self.page.height:
                new_height = self.page.height // 6
                header.dimension = (self.page.width, new_height)
            header.draw()
        else:
            raise ValueError('header must be FontPreview based object')

# endregion
