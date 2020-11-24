<img src="https://fontpreview.readthedocs.io/en/latest/_static/fp.png" alt="fontpreview package">
<br>
# fontpreview: Python library for font previews

> This module is under development

This is a library that allows you to create preview images from one or more selected fonts.

Full docs is here: [ReadTheDocs](https://fontpreview.readthedocs.io/en/latest/)

## Installation

Use Pypi:
```console
$ pip install --user fontpreview
```

## Simple usage

Preview example:
```python
from fontpreview import FontPreview

fp = FontPreview('/tmp/noto.ttf')
fp.save('/tmp/fp.png')
```
<img src="https://i.ibb.co/258dCPZ/fp.png" alt="FontPreview object" width="350" height="150">
<br><br>

Banner example:
```python
from fontpreview import FontBanner

fb = FontBanner('/tmp/noto.ttf', 'landscape', bg_color=(153, 153, 255), mode='fontname')
fb.save('/tmp/fb.png')
```
<img src="https://i.ibb.co/FVWdkYC/fb.png" alt="FontBanner object" width="350" height="130">
<br><br>

Logo example:
```python
from fontpreview import FontLogo

fl = FontLogo('/tmp/noto.ttf', 'Fp')
fl.save('/tmp/fl.png')
```
<img src="https://i.ibb.co/j302Y5k/fl.png" alt="FontLogo object">
<br><br>

Font wall example:
```python
from fontpreview import FontBanner, FontWall

# Define the various parts of wall
fb = FontBanner('/tmp/noto.ttf', 'landscape' , mode='fontname')
fb2 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='alpha')
fb3 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='letter')
fb4 = FontBanner('/tmp/noto.ttf', 'landscape' , mode='paragraph')
fw = FontWall([fb,fb2,fb3,fb4])
fw.save('/tmp/fw.png')
```
<img src="https://i.ibb.co/cDBST2r/fw.png" alt="FontWall object" width="650" height="200">
<br><br>


Font page example:
```python
from fontpreview import FontPage, FontBanner

# Define the various parts of page
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

```
<img src="https://i.ibb.co/LgFLnXk/fpage.png" alt="FontPage object" width="650" height="850">
<br><br>

Font page with template example:
```python
from fontpreview import FontPage, FontPageTemplate, FontBanner

# Define the various parts of page
header = FontBanner('/tmp/noto.ttf', 'landscape' , mode='fontname')
body = FontBanner('/tmp/noto.ttf', 'landscape' , mode='paragraph')
footer = FontBanner('/tmp/noto.ttf', 'landscape' , mode='letter')
# Create font page template
template = FontPageTemplate(3508)
template.set_body(170, 1, 'lcenter')
template.set_footer(100, 4, 'lcenter')
# Create FontPage object
fpage = FontPage(template=template)
fpage.set_header(header)
fpage.set_body(body)
fpage.set_footer(footer)
# Design all parts
fpage.draw()
fpage.save('/tmp/fpage_template.png')

```
<img src="https://i.ibb.co/qJjMGpr/fpage-template.png" alt="FontPage with template object" width="650" height="850">
<br><br>

## Advanced usage

Below is an example of various previews of the _"Fira Code regular"_ font. 
Does it remind you of anything? [Fira code original](https://github.com/tonsky/FiraCode/raw/master/extras/logo.svg)
```python
# FIRA CODE WALL
from fontpreview import FontBanner, FontWall
fira_code = '/tmp/firacode.ttf'
# RGB group = ('background', 'FIRA COD color', 'Ligature color', 'E color background')
colors_group = [
                ('black', (0, 143, 0), (0, 236, 236), (255, 0, 255)),
                ('black', (166, 47, 123), (81, 208, 93), (11, 179, 248)),
                ((13, 21, 43), (112, 204, 84), (226, 110, 34), (223, 245, 90)),
                ((43, 6, 42), (136, 126, 135), (4, 150, 153), (147, 103, 145)),
                ((39, 57, 85), (255, 241, 208), (208, 84, 0), (209, 215, 227)),
                ((31, 63, 89), (248, 248, 242), (230, 219, 117), (166, 226, 51)),
                ((1, 47, 80), (224, 202, 52), (73, 217, 38), (255, 125, 158)),
                ((0, 0, 170), (75, 224, 245), (255, 255, 85), (0, 170, 170)),
                ('white', 'black', 'black', 'black'),
                ((247, 247, 247), (167, 29, 93), (121, 93, 163), (0, 134, 179)),
                ((239, 240, 243), (15, 131, 207), (208, 84, 0), (105, 40, 122)),
                ((239, 231, 212), (218, 116, 53), (0, 142, 212), (186, 136, 0)),
                ((39, 40, 34), (132, 214, 45), (249, 39, 114), (174, 129, 255)),
                ((43, 48, 59), (180, 142, 173), (143, 161, 179), (152, 190, 140)),
                ((32, 32, 32), (171, 130, 84), (160, 171, 127), (216, 127, 98)),
                ((0, 43, 54), (0, 160, 153), (126, 143, 3), (218, 66, 130))
                ]
banners = []
# Create banners
for colors in colors_group:
    # Create a FontBanner objects
    fb = FontBanner(fira_code, (413, 240))
    liga = FontBanner(fira_code, (413, 240))
    E = FontBanner(fira_code, (40, 70))
    # Set background colors
    fb.bg_color = liga.bg_color = colors[0]
    E.bg_color = colors[3]
    # Set foreground colors
    fb.fg_color = colors[1]
    liga.fg_color = colors[2]
    E.fg_color = colors[0]
    # Set text
    fb.font_text = 'FIRA COD'
    liga.font_text = "!=->>++:="
    E.font_text = 'E'
    # Set text position
    E.set_text_position('ltop')
    fb.set_text_position((25, 60))
    liga.set_text_position('top')
    # Adding image on fb
    fb.add_image(liga, (0, 122))
    fb.add_image(E, (339, 60))
    # Add to list of banners
    banners.append(fb)

# Create a wall
fw = FontWall(banners, max_tile=4)
fw.save('/tmp/fira_code.png')
```
<img src="https://i.ibb.co/cvnPRdB/fira-code.png" alt="Fira code wall">
<br><br>

## Open source
_fontpreview_ is a open source project. Any contribute, It's welcome.

**A great thanks**.

For donations, press this

For me

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/guos)

For [Telethon](http://www.telethon.it/)

The Telethon Foundation is a non-profit organization recognized by the Ministry of University and Scientific and Technological Research.
They were born in 1990 to respond to the appeal of patients suffering from rare diseases.
Come today, we are organized to dare to listen to them and answers, every day of the year.

<a href="https://www.telethon.it/sostienici/dona-ora"> <img src="https://www.telethon.it/dev/_nuxt/img/c6d474e.svg" alt="Telethon" title="Telethon" width="200" height="104" /> </a>

[Adopt the future](https://www.ioadottoilfuturo.it/)


## Acknowledgments

Thanks to Mark Lutz for writing the _Learning Python_ and _Programming Python_ books that make up my python foundation.

Thanks to Kenneth Reitz and Tanya Schlusser for writing the _The Hitchhiker’s Guide to Python_ books.

Special thanks go to my wife, who understood the hours of absence for this development. 
Thanks to my children, for the daily inspiration they give me and to make me realize, that life must be simple.

Thanks Python!
