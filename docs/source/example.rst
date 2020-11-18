Example
#######

Here are some examples that allow basic and advanced use of the library.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

FontPreview example
*******************

FontPreview is a class that creates objects that allow the representation of a font in an image.
By default, it creates a white rectangle with a preview of the letters *a b c d e f* in black.

.. code-block:: python

    from fontpreview import FontPreview
    fp = FontPreview('/tmp/noto.ttf')   # path of font file
    fp.save('/tmp/fp.png')              # default directory is working directory

This is result:

.. image:: https://i.ibb.co/258dCPZ/fp.png
    :alt: FontPreview image

Now, let's modify some properties.

.. code-block:: python

    fp.font_text = 'Welcome to fontpreview'
    fp.bg_color = (253, 194, 45)        # Background color. RGB color: yellow
    fp.dimension = (300, 250)           # specify dimension in pixel: 300 x 250
    fp.fg_color = (51, 153, 193)        # Foreground or font color. RGB color: blue
    fp.set_font_size(50)                # set font size to 50 pixel
    fp.set_text_position('ltop')        # place the text at the top left.
    # before saving the image, you need to draw it again
    fp.draw()
    fp.save('/tmp/fp.png')


.. image:: https://i.ibb.co/0rY6YqR/fp.png
    :alt: FontPreview image
