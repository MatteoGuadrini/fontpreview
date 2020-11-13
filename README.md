# fontpreview: Python library for font previews

> This module is under development

This is a library that allows you to create preview images from one or more selected fonts.

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

```
<img src="https://i.ibb.co/LgFLnXk/fpage.png" alt="FontWall object" width="650" height="850">
<br><br>

Font page with template example:
```python
from fontpreview import FontPage, FontPageTemplate, FontBanner

# Define the various parts of wall
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
<img src="https://i.ibb.co/qJjMGpr/fpage-template.png" alt="FontWall object" width="650" height="850">
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
