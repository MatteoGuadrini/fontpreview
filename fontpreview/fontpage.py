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
from .fontbanner import FontLogo
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

    def set_logo(self, logo):
        """
        Set logo of Font page
        :param logo: FontLogo object
        :return: None
        """
        # Check if logo is FontLogo object
        if isinstance(logo, FontLogo):
            # Check if header exists
            if self.header:
                # Check size of header
                if self.header.image.size < logo.image.size:
                    logo.new_size((75, 75))
                # Add logo on header
                self.header.add_image(logo, CALC_POSITION['lcenter'](self.header.dimension,
                                                                     self.header.font.getsize(self.header.font_text)))
            else:
                raise AttributeError('header attribute is None')
        else:
            raise ValueError('logo must be FontLogo object')

    def set_body(self, body):
        """
        Set body of Font page
        :param body: FontPreview object
        :return: None
        """
        # Check if body is FontPreview object
        if isinstance(body, FontPreview):
            # Check width of body
            if self.page.width != body.image.width:
                body.dimension = (self.page.width, body.image.height)
                body.font_position = CALC_POSITION['center'](body.dimension, body.font.getsize(body.font_text))
            self.body = body
            # Check height of body
            if body.image.height > self.page.height:
                new_height = self.page.height // 3
                body.dimension = (self.page.width, new_height)
            body.draw()
        else:
            raise ValueError('body must be FontPreview based object')

    def set_footer(self, footer):
        """
        Set footer of Font page
        :param footer: FontPreview object
        :return: None
        """
        # Check if footer is FontPreview object
        if isinstance(footer, FontPreview):
            # Check width of footer
            if self.page.width != footer.image.width:
                footer.dimension = (self.page.width, footer.image.height)
                footer.font_position = CALC_POSITION['center'](footer.dimension, footer.font.getsize(footer.font_text))
            self.footer = footer
            # Check height of footer
            if footer.image.height > self.page.height:
                new_height = self.page.height // 4
                footer.dimension = (self.page.width, new_height)
            footer.draw()
        else:
            raise ValueError('body must be FontPreview based object')

# endregion