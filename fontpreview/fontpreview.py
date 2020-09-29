#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# fontpreview -- fontpreview
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
from PIL import Image, ImageDraw, ImageFont

# endregion

# region variable
CALC_POSITION = {
    'center': lambda ixy, fxy: ((ixy[0] - fxy[0]) / 2, (ixy[1] - fxy[1]) / 2),
    'top': lambda ixy, fxy: ((ixy[0] - fxy[0]) / 2, 0),
    'below': lambda ixy, fxy: ((ixy[0] - fxy[0]) / 2, (ixy[1] - fxy[1])),
    'rcenter': lambda ixy, fxy: ((ixy[0] - fxy[0]), (ixy[1] - fxy[1]) / 2),
    'rtop': lambda ixy, fxy: ((ixy[0] - fxy[0]), 0),
    'rbelow': lambda ixy, fxy: ((ixy[0] - fxy[0]), (ixy[1] - fxy[1])),
    'lcenter': lambda ixy, fxy: (0, (ixy[1] - fxy[1]) / 2),
    'ltop': lambda ixy, fxy: (0, 0),
    'lbelow': lambda ixy, fxy: (0, (ixy[1] - fxy[1])),
}


# endregion

# region classes
class FontPreview:
    """
    Class that represents the preview of a font
    """

    def __init__(self, font):
        """
        Object that represents the preview of a font
        :param font: font file
        """
        # Define properties
        self.image = None
        self.font_size = 64
        self.font_text = 'a b c d e f'
        self.font = ImageFont.truetype(font=font, size=self.font_size)
        self.color_system = 'RGB'
        self.bg_image = None
        self.bg_color = 'white'
        self.fg_color = 'black'
        self.dimension = (700, 327)
        self.font_position = CALC_POSITION['center'](self.dimension, self.font.getsize(self.font_text))
        # Create default image
        self.draw()

    def save(self, path=os.path.join(os.path.abspath(os.getcwd()), 'fontpreview.png')):
        """
        Save the preview font
        :param path: path where you want to save the preview font
        :return: None
        """
        self.image.save(path)

    def draw(self, align='left'):
        """
        Draw image with text based on properties of this object
        :param align: alignment of text. Available 'left', 'center' and 'right'
        :return: None
        """
        # Set an image
        if self.bg_image:
            self.image = Image.open(self.bg_image)
            draw = ImageDraw.Draw(self.image)
            draw.text(self.font_position, self.font_text, fill=self.fg_color, font=self.font, align=align)
        # Draw background with flat color
        else:
            self.image = Image.new(self.color_system, self.dimension, color=self.bg_color)
            draw = ImageDraw.Draw(self.image)
            draw.text(self.font_position, self.font_text, fill=self.fg_color, font=self.font, align=align)

    def set_font_size(self, size):
        """
        Set size of font
        :param size: size of font
        :return: None
        """
        # Set size of font
        self.font_size = size
        self.font = ImageFont.truetype(font=self.font.path, size=self.font_size)
        # Create default image
        self.draw()

    def set_text_position(self, position):
        """
        Set position of text
        :param position: Position can be a tuple with x and y axis, or a string.
        The strings available are 'center', 'top', 'below', 'rcenter', 'rtop', 'rbelow', 'lcenter', 'ltop' and 'lbelow'.
        :return: None
        """
        if isinstance(position, tuple):
            self.font_position = position
        else:
            self.font_position = CALC_POSITION.get(position, 'center')(
                self.dimension, self.font.getsize(self.font_text)
            )
        # Create default image
        self.draw()

# endregion
