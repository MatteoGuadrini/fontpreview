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
from PIL import Image, ImageDraw, ImageFont


# endregion

# region classes
class FontPreview:
    def __init__(self, font):
        """
        Object that represents the preview of a font
        :param font: font name or font file
        """
        # Define properties
        self.font_size = 64
        self.font_text = 'a b c d e f'
        self.font_position = (200, 140)
        self.font = ImageFont.truetype(font=font, size=self.font_size)
        self.color_system = 'RGB'
        self.bg_image = None
        self.bg_color = 'white'
        self.fg_color = 'black'
        self.dimension = (700, 327)
        # Create default image
        self.image = Image.new(self.color_system, self.dimension, color=self.bg_color)
        draw = ImageDraw.Draw(self.image)
        draw.text(self.font_position, self.font_text, fill=self.fg_color, font=self.font)

# endregion
