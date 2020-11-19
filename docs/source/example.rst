Example
#######

Here are some examples that allow basic and advanced use of the library.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

FontPreview example
*******************

*FontPreview* is a class that creates objects that allow the representation of a font in an image.
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

A background image can also be set.

.. code-block:: python

    fp.bg_image = '/tmp/python.png'     # a background image
    fp.draw()                           # draw it again
    fp.save('/tmp/fp.png')

.. image:: https://i.ibb.co/RScSMvQ/fp.png
    :alt: FontPreview image

FontBanner example
******************

*FontBanner* is a FontPreview-based class, which adds some features to work with one or more objects based on the FontPreview class.
With this object since its creation, it is possible to define the orientation: *landscape* or *portrait*.

.. code-block:: python

    from fontpreview import FontBanner
    fb = FontBanner('/tmp/noto.ttf', 'landscape', bg_color=(253, 194, 45))   # path of font file
    fb.save('/tmp/fb.png')

.. image:: https://i.ibb.co/MPJ1Dr8/fb.png
    :alt: FontBanner image

Let's go and change some of the properties.

.. code-block:: python

    fb.set_mode('fontname')         # set font_text properties to font name
    fb.set_orientation('portrait')  # set vertical orientation of image
    fb.save('/tmp/fb.png')

.. image:: https://i.ibb.co/RgLSZC1/fb.png
    :alt: FontBanner image
    :height: 700

And now, let's add the *FontPreview* object created earlier.

.. code-block:: python

    fb.font_text = 'Python'
    fb.set_font_size(50)            # change font size: FontPreview method
    fb.bg_color = 'white'           # set color with name string
    fb.set_orientation((300, 800))  # change orientation and size again with tuple
    fb.draw()                       # draw it again
    fb.add_image(fp, (0, 150))      # add FontPreview object to FontBanner object
    fb.save('/tmp/fb.png')

.. image:: https://i.ibb.co/rfMwd7R/fb.png
    :alt: FontBanner image