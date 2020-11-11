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
import os
from .fontpreview import FontPreview, CALC_POSITION
from .fontbanner import FontLogo
from PIL import Image, ImageDraw


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

    def __compose(self):
        """
        Dynamically compose the page
        :return: None
        """
        # Check if the template is specified
        if self.template:
            pass
        else:
            # Define font position for each part
            text_position = 'center'
            # Define font size for each part
            header_font_size = 120
            body_font_size = 140
            footer_font_size = 120
            # Divide the size into six equal parts
            unit = self.page.height // 6
            # I define the units for each part of the page
            header_units = unit
            body_units = unit * 3
            footer_units = unit * 2
            # Check height of each part
            if self.header.image.height != header_units:
                self.header.dimension = (self.page.width, header_units)
                self.header.set_font_size(header_font_size)
                self.header.set_text_position(text_position)
            if self.body.image.height != body_units:
                self.body.dimension = (self.page.width, body_units)
                self.body.set_font_size(body_font_size)
                self.body.set_text_position(text_position)
            if self.footer.image.height != footer_units:
                self.footer.dimension = (self.page.width, footer_units)
                self.footer.set_font_size(footer_font_size)
                self.footer.set_text_position(text_position)

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
                header.draw()
            self.header = header
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
                body.draw()
            self.body = body
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
                footer.draw()
            self.footer = footer
        else:
            raise ValueError('footer must be FontPreview based object')

    def draw(self, separator=True, sep_color='black', sep_width=5):
        """
        Draw font page with header, logo, body and footer
        :param separator: line that separates the parts
        :param sep_color: separator color
        :param sep_width: separator width
        :return: None
        """
        # Compose all parts
        self.__compose()
        header_start = (0, 0)
        self.page.paste(self.header.image, header_start)
        body_start = (0, self.header.image.height)
        self.page.paste(self.body.image, body_start)
        footer_start = (0, (self.body.image.height + self.header.image.height))
        self.page.paste(self.footer.image, footer_start)
        # Draw line
        if separator:
            draw = ImageDraw.Draw(self.page)
            # Header/Body line
            body_finish = (self.page.width, self.header.image.height)
            draw.line([body_start, body_finish], fill=sep_color, width=sep_width)
            # Body/Footer line
            footer_finish = (self.page.width, self.body.image.height + self.header.image.height)
            draw.line([footer_start, footer_finish], fill=sep_color, width=sep_width)

    def save(self, path=os.path.join(os.path.abspath(os.getcwd()), 'fontpage.png')):
        """
        Save the font page
        :param path: path where you want to save the font page
        :return: None
        """
        self.page.save(path)


class FontPageTemplate:
    """
    Class representing the template of a FontPage object
    """

    def __init__(self, page_height, units_number=6):
        """
        Object representing the template of a FontPage object
        :param page_height: height of FontPage object
        :param units_number: division number to create the units
        """
        # Calculate units
        self.unit = page_height // units_number
        # header
        self.header_font_size = 120
        self.header_units = self.unit
        self.header_text_position = 'center'
        # body
        self.body_font_size = 140
        self.body_units = self.unit * 3
        self.body_text_position = 'center'
        # footer
        self.footer_font_size = 120
        self.footer_units = self.unit * 2
        self.footer_text_position = 'center'

    def set_header(self, font_size, units, text_position):
        """
        Setting the header properties
        :param font_size: the header font size
        :param units: the header units number
        :param text_position: the header text position
        :return: None
        """
        # header
        self.header_font_size = font_size
        self.header_units = self.unit * units
        self.header_text_position = text_position

    def set_body(self, font_size, units, text_position):
        """
        Setting the body properties
        :param font_size: the body font size
        :param units: the body units number
        :param text_position: the body text position
        :return: None
        """
        # header
        self.body_font_size = font_size
        self.body_units = self.unit * units
        self.body_text_position = text_position


# endregion
