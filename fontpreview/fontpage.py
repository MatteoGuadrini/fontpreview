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

# region Imports
from .fontpreview import FontPreview, CALC_POSITION
from .fontbanner import FontBanner, FontLogo
from PIL import Image


# endregion

# region Classes
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

# endregion
