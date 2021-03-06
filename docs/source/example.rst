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
    fp.bg_color = (253, 194, 45)        # background color. RGB color: yellow
    fp.dimension = (300, 250)           # specify dimension in pixel: 300 x 250
    fp.fg_color = (51, 153, 193)        # foreground or font color. RGB color: blue
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


FontLogo example
****************

*FontLogo* is a FontPreview-based class, which represents a square where inside there are one or two letters.
The fontpreview package logo was generated with this class.

.. code-block:: python

    from fontpreview import FontLogo
    fl = FontLogo('/tmp/noto.ttf', 'Fp')    # specify font and letters. Max 2
    fl.save('/tmp/fl.png')

.. image:: https://i.ibb.co/j302Y5k/fl.png
    :alt: FontLogo image

Being a FontPreview based object, it inherits all its characteristics.

.. code-block:: python

    fl.font_text = 'TS'
    fl.bg_color = (45, 121, 199)    # background color. RGB color: blue
    fl.fg_color = 'white'           # foreground color. RGB color: white
    fl.set_text_position('rbelow')  # position is "right-below"
    fl.save('/tmp/fl.png')

.. image:: https://i.ibb.co/MSFRkfP/fl.png
    :alt: FontLogo image

FontWall example
****************

*FontWall* is a class that represents an image in which there are multiple objects based on the FontPreview class.

This object accepts a list of font paths (with which it automatically builds FontBanner objects) or a list of objects based on the FontPreview class.

The FontWall object has a mode, which can be *horizontal* or *vertical*, or just specify the usual tuple of with x and y (x, y) axis.
It also accepts a maximum of tiles per row (if the orientation is horizontal) or column (if the orientation is vertical).

.. code-block:: python

    from fontpreview import FontBanner, FontWall
    # Define the various parts of wall
    fb = FontBanner('/tmp/noto.ttf', 'landscape' , mode='fontname')
    fb2 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='alpha')
    fb3 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='letter')
    fb4 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='paragraph')
    fw = FontWall([fb,fb2,fb3,fb4])
    fw.save('/tmp/fw.png')

.. image:: https://i.ibb.co/cDBST2r/fw.png
    :alt: FontWall image

Any changes made on the parts of the wall are made to the final result.

.. code-block:: python

    # Modify properties of first banner
    fb.font_text = 'Harry Potter'
    fb.bg_color = (43, 43, 43)
    fb.fg_color = 'white'
    fb.set_font_size(120)
    # Modify properties of second banner
    fb2.font_text = 'Harry Potter is a series of seven fantasy novels\nwritten by British author J. K. Rowling.'
    fb2.bg_color = (150, 45, 46)
    fb2.fg_color = 'white'
    fb2.set_font_size(100)
    fb2.set_text_position('ltop')
    # Modify properties of third banner
    fb3.font_text = 'The series was originally published in English by two major publishers,\nBloomsbury in the United Kingdom and Scholastic Press in the United States. '
    fb3.bg_color = (63, 55, 36)
    fb3.fg_color = 'white'
    fb3.set_font_size(100)                  # the font is resized automatically because it exceeds the size of the banner
    fb3.set_text_position('rcenter')
    # Modify properties of last banner
    fb4.font_text = 'A series of many genres, including fantasy, drama,\ncoming of age, and the British school story'
    fb4.bg_color = (205, 193, 87)
    fb4.fg_color = 'black'
    fb4.set_font_size(100)
    fb4.set_text_position('rbelow')
    fw.draw(2)                           # draw it again, specify max_tile
    fw.save('/tmp/fw.png')

.. image:: https://i.ibb.co/W0B3LYn/fw.png
    :alt: FontWall image

FontPage example
****************

*FontPage* is a class that represents a sample page per font. This object consists of three parts: header, body and footer.
These three parts have a standard size defined by a FontPageTemplate (see below).

.. code-block:: python

    from fontpreview import FontPage, FontBanner
    # Define the various parts of wall
    header = FontBanner('/tmp/noto.ttf', 'landscape' , mode='fontname')
    body = FontBanner('/tmp/noto.ttf', 'landscape' , mode='paragraph')
    footer = FontBanner('/tmp/noto.ttf', 'landscape' , mode='letter')
    # Create FontPage object
    fpage = FontPage()
    fpage.set_header(header)
    fpage.set_body(body)
    fpage.set_footer(footer)
    # Design all parts
    fpage.draw()
    fpage.save('/tmp/fpage.png')

.. image:: https://i.ibb.co/LgFLnXk/fpage.png
    :alt: FontPage image

Even with this object, any changes made to the individual parts of the page appear in the final result.

It is also possible to add a FontLogo object to the header, after the header has been defined.

.. code-block:: python

    from fontpreview import FontLogo
    fl = FontLogo('/tmp/noto.ttf', 'Fp')    # create logo
    fpage.set_logo(fl)                      # set logo on header
    fpage.body.bg_color = (253, 194, 45)
    fpage.body.set_font_size(150)
    fpage.draw()
    fpage.save('/tmp/fpage.png')

.. image:: https://i.ibb.co/dtt9Ct7/fpage.png
    :alt: FontPage image

FontPageTemplate example
************************

*FontPageTemplate* is a class that represents a template applicable to the FontPage object.

In this object, only the specifications of each part of the FontPage object (header, body, footer) are defined: font size, text position, unit.

The units (default 6) are equal parts divided across the height of the page.

.. code-block:: python

    from fontpreview import FontPageTemplate
    template = FontPageTemplate(3508)           # max height of page
    template.set_body(170, 1, 'lcenter')        # font_size, units, text_position
    template.set_footer(100, 4, 'lcenter')      # font_size, units, text_position
    # Create FontPage object
    fpage = FontPage(template=template)
    fpage.set_header(header)
    fpage.set_body(body)
    fpage.set_footer(footer)
    # Design all parts
    fpage.draw()
    fpage.save('/tmp/fpage_template.png')

.. image:: https://i.ibb.co/n7L9nNG/fpage-template.png
    :alt: FontPage image

FontBooklet example
*******************

*FontBooklet* is a class that represents a book of *FontPage* object.

.. code-block:: python

    from fontpreview import FontPage, FontBanner, FontBooklet
    # Define the various parts of page
    header = FontBanner('/tmp/noto.ttf', 'landscape' , mode='fontname')
    body = FontBanner('/tmp/noto.ttf', 'landscape' , mode='paragraph')
    footer = FontBanner('/tmp/noto.ttf', 'landscape' , mode='letter')
    # Create FontPage object
    fpage1 = FontPage(header=header, body=body, footer=footer)
    fpage2 = FontPage(header=header, body=body, footer=footer)
    # Design all parts
    fpage1.draw()
    fpage2.draw()
    # Create book
    book = FontBooklet(fpage1, fpage2)
    book.save('/tmp/noto_book/')        # save page1.png, page2.png in /tmp/noto_book/ folder


Declarative object creation
***************************

Each *FontPreview* and *FontPage* based object in this module has a declarative instance implementation.

.. code-block:: python

    from fontpreview import FontPreview, FontBanner, FontLogo, FontPage
    # FontPreview object
    fp = FontPreview('/tmp/noto.ttf',
                    font_size=50,
                    font_text='some text',
                    color_system='RGB',
                    bg_color='blue',
                    fg_color='yellow',
                    dimension=(800, 400))
    # FontBanner object
    fb = FontBanner('/tmp/noto.ttf',
                    orientation='portrait',
                    bg_color='blue',
                    fg_color='yellow',
                    mode='paragraph',
                    font_size=70,
                    color_system='RGB')
    # FontLogo object
    fl = FontLogo('/tmp/noto.ttf',
                    'Fl',
                    size=(170, 170),
                    bg_color='yellow',
                    fg_color='blue',
                    font_size=50,
                    color_system='RGB')
    # FontPage object
    page = FontPage(header=fb, logo=fl, body=fb, footer=fb)
    page.draw()
