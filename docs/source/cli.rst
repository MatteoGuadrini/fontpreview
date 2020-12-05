Command line
############

Here we explain how to use the *fontpreview* tool on the command line

.. note::
    If you want to use the command line tool, you need to install the system-wide library: ``pip install fontpreview``

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is help system:

.. code-block:: console

    $ fp --help
    usage: fp [-h] [--verbose] [--version] [-t TEXT] [-b BG_COLOR] [-f FG_COLOR] [-i IMAGE]
              [-d DIMENSION DIMENSION] [-s SAVE_PATH] [-p TEXT_POSITION] [-z SIZE]
              font

    FontPreview cli

    positional arguments:
      font                  font file path

    optional arguments:
      -h, --help            show this help message and exit
      --verbose, -v         enable verbosity, for debug
      --version, -V         show program's version number and exit
      -t TEXT, --text TEXT  text include to preview image (default: a b c d e f)
      -b BG_COLOR, --background BG_COLOR
                            background color (default: white)
      -f FG_COLOR, --foreground FG_COLOR
                            foreground color (default: black)
      -i IMAGE, --background-image IMAGE
                            background image path
      -d DIMENSION DIMENSION, --dimension DIMENSION DIMENSION
                            dimension x and y (default: 700x327)
      -s SAVE_PATH, --save SAVE_PATH
                            save file path (default: current directory)
      -p TEXT_POSITION, --text-position TEXT_POSITION
                            save file path (default: center)
      -z SIZE, --size SIZE  size of font (default: 64)


Simple usage
************

Save *fontpreview* image in a current directory from font file:

.. code-block:: console

    $ fp /tmp/noto.ttf

.. image:: https://i.ibb.co/258dCPZ/fp.png
    :alt: FontPreview image

Advanced usage
**************

Use ``-v`` for debugging; ``-d`` setting dimension with **x** and **y** axis; ``-b`` setting background colors,
``-f`` setting foreground colors, ``-p`` setting text position, ``-z`` setting font size and ``-s`` specified file path to save.

For the color reference: `colors <https://github.com/python-pillow/Pillow/blob/master/src/PIL/ImageColor.py>`_

.. code-block:: console

    $ fp /tmp/noto.ttf -v -t 'Hello Noto' -d 1000 1000 -b 'green' -f 'blue' -p 'lcenter' -z 50 -s /tmp/fp.png
    DEBUG: set text position: "lcenter"
    DEBUG: font object => font_name:('Noto Sans', 'Regular'),font_size:50,text:Hello Noto,text_position:(0, 473),dimension:(1000, 1000)

.. image:: https://i.ibb.co/SfSmX44/fp.png
    :alt: FontPreview image