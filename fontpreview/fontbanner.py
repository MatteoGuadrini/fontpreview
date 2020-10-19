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

# region imports
import os
from .fontpreview import FontPreview, CALC_POSITION
from PIL import Image


# endregion

# region functions
def resize(image, size):
    """
    Resize image
    :param image: image to resize
    :param size: new size of image
    :return: Image
    """
    # Resize image
    return image.resize(size)


# endregion

# region classes
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

    def __str__(self):
        """
        String representation of font banner
        :return: string
        """
        return FontPreview.__str__(self) + ",mode={mode}".format(mode=self.mode)

    def set_orientation(self, orientation, font_position='center'):
        """
        Set orientation of banner
        :param orientation: the orientation of the banner; 'landscape' or 'portrait'
        :param font_position: font position respect dimension of banner
        :return: None
        """
        # Calculate banner size
        if isinstance(orientation, tuple):
            self.dimension = orientation
            # Recalculate font position
            self.set_text_position(font_position)
            return None
        else:
            LANDSCAPE = (1653, 560)
            PORTRAIT = (560, 1653)
            if orientation == 'landscape':
                self.dimension = LANDSCAPE
            elif orientation == 'portrait':
                self.dimension = PORTRAIT
            else:
                raise ValueError('orientation is "landscape","portrait" or tuple(x,y)')
            # Recalculate font position
            self.set_text_position(font_position)

    def set_mode(self, mode, align='center'):
        """
        Set the text mode
        :param mode: mode that sets the text in the banner
        :param align: alignment of text. Available 'left', 'center' and 'right'
        :return: None
        """
        MODE = {
            'letter': 'a b c d e f\ng h i j k l\nm n o p q r\ns t u v w x y z',
            'alpha': 'Aa Bb Cc Dd Ee Ff\n1 2 3 4 5 6 7 8 9 0',
            'fontname': '{0}'.format(self.font.getname()[0]),
            'paragraph': 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',
            'combination': '{0}\n{1}'.format(self.font.getname(),
                                             'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.'
                                             ),
            'none': ''
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
        if isinstance(image, FontPreview):
            img = image.image
        else:
            img = Image.open(image)
        # Check if the image is bigger than the banner
        if img.size > self.dimension:
            width, height = self.dimension
            img = resize(img, (width // 2, height // 2))
        # Add image
        self.image.paste(img, position)


class FontWall:
    """
    Class that represents the wall of fonts
    """

    def __init__(self, fonts, max_tile=2, mode='horizontal'):
        """
        Object that represents the wall of fonts
        :param fonts: font list; string or FontPreview object
        :param max_tile: maximum tile per row/column
        :param mode: image alignment, 'horizontal' or 'vertical'
        """
        # Check if list contains string or FontPreview object
        if isinstance(fonts, list):
            self.fonts = []
            for font in fonts:
                if isinstance(font, FontPreview):
                    self.fonts.append(font)
                else:
                    _font = FontBanner(font)
                    self.fonts.append(_font)
        else:
            raise TypeError("'fonts' must be a list")
        # Other properties
        self.color_system = 'RGB'
        self.bg_color = 'white'
        self.max_width = None
        self.max_height = None
        self.mode = mode
        self.max_tile = max_tile
        # Build the wall
        self.wall = None
        self.draw(self.max_tile)

    def __str__(self):
        """
        String representation of font wall
        :return: string
        """
        return str(["tile{0}={1}".format(i, f) for i, f in enumerate(self.fonts)])

    def __concatenate(self, fonts, position):
        """
        Link multiple images to form a layout inside the wall
        :param fonts: list of FontPreview
        :param position: paste positions
        :return: tuple
        """
        # Get max width and height, presume horizontal
        if self.mode == 'horizontal':
            max_width = sum([font.image.width for font in fonts])
            max_height = max([font.image.height for font in fonts])
        else:
            max_width = max([font.image.width for font in fonts])
            max_height = sum([font.image.height for font in fonts])
        # Create background
        dst = Image.new(self.color_system, (max_width, max_height))
        start = 0
        for font in fonts:
            # Compose the row
            if self.mode == 'horizontal':
                dst.paste(font.image, (start, 0))
                start = font.image.width + start
            # Compose the column
            elif self.mode == 'vertical':
                dst.paste(font.image, (0, start))
                start = font.image.height + start
            else:
                raise ValueError("the mode can be 'horizontal' or 'vertical'")
        self.wall.paste(dst, position)
        return dst.size

    def draw(self, max_tile):
        """
        Draw wall with fonts on properties of this object
        :param max_tile: maximum tile per row
        :return: None
        """
        # Split fonts into maximum tile per row/column
        fonts = []
        for i in range(0, len(self.fonts), max_tile):
            fonts.append(self.fonts[i:i + max_tile])
        # Calculate max_width and max_height of wall
        max_width = []
        max_height = []
        for font in fonts:
            if self.mode == 'horizontal':
                max_width.append(sum([f.image.width for f in font]))
                max_height.append(max([f.image.height for f in font]))
            else:
                max_width.append(max([f.image.width for f in font]))
                max_height.append(sum([f.image.height for f in font]))
        if self.mode == 'horizontal':
            self.max_width = max(max_width)
            self.max_height = sum(max_height)
        else:
            self.max_width = sum(max_width)
            self.max_height = max(max_height)
        self.wall = Image.new(self.color_system, (self.max_width, self.max_height), color=self.bg_color)
        # Build the wall
        start_position = (0, 0)
        for font in fonts:
            if self.mode == 'horizontal':
                last_position = self.__concatenate(font, start_position)
                start_position = (0, (start_position[1] + last_position[1]))
            else:
                last_position = self.__concatenate(font, start_position)
                start_position = ((start_position[0] + last_position[0]), 0)

    def save(self, path=os.path.join(os.path.abspath(os.getcwd()), 'fontwall.png')):
        """
        Save the font wall
        :param path: path where you want to save the font wall
        :return: None
        """
        self.wall.save(path)

# endregion
