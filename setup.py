#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# setup -- fontpreview
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

from distutils.core import setup
VERSION = '0.8.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fontpreview',
    version=VERSION,
    packages=['fontpreview'],
    url='https://github.com/matteoguadrini/fontpreview',
    license='GNU General Public License v3.0',
    author='Matteo Guadrini',
    author_email='matteo.guadrini@hotmail.it',
    keywords='fontpreview library font previews',
    maintainer='Matteo Guadrini',
    maintainer_email='matteo.guadrini@hotmail.it',
    install_requires=['Pillow'],
    description='Python library for font previews',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv3 License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6'
)
