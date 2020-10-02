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
from PIL import Image


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
        self.set_mode(mode=mode)

    def set_orientation(self, orientation, font_position='center'):
        """
        Set orientation of banner
        :param orientation: the orientation of the banner; 'landscape' or 'portrait'
        :param font_position: font position respect dimension of banner
        :return: None
        """
        LANDSCAPE = (1653, 560)
        PORTRAIT = (560, 1653)
        # Calculate banner size
        if isinstance(orientation, tuple):
            self.dimension = orientation
            # Recalculate font position
            self.set_text_position(font_position)
            return None
        if orientation == 'landscape':
            self.dimension = LANDSCAPE
        elif orientation == 'portrait':
            self.dimension = PORTRAIT
        else:
            raise ValueError('orientation is "landscape","portrait" or tuple(x,y)')
        # Recalculate font position
        self.set_text_position(font_position)
        # Create default image
        self.draw()

    def set_mode(self, mode, align='center'):
        """
        Set the text mode
        :param mode: mode that sets the text in the banner
        :param align: alignment of text. Available 'left', 'center' and 'right'
        :return: None
        """
        MODE = {
            'letter': 'abcdef\nghijkl\nmnopqr\nstuvwxyz',
            'alpha': 'Aa Bb Cc Dd Ee Ff\n1 2 3 4 5 6 7 8 9 0',
            'fontname': self.font.getname(),
            'paragraph': 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',
            'combination': '{0}\n{1}'.format(self.font.getname(),
                                             'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.'
                                             )
        }
        # Verify is mode exists
        if mode in MODE:
            self.mode = mode
            self.font_text = MODE.get(mode)
            # Create default image
            self.draw(align=align)
        else:
            raise ValueError('mode is "letter", "alpha", "fontname", "paragraph" and "combination"')

    def add_image(self, image, position):
        """
        Adds an additional image to the banner
        :param image: path of image
        :param position: position of image
        :return: None
        """
        # Create image
        img = Image.open(image)
        # Add image
        self.image.paste(img, position)
