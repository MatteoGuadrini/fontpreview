# fontpreview: Python library for font previews

> This module is under development

This is a library that allows you to create preview images from one or more selected fonts.

Simple example:
```python
from fontpreview import FontPreview

fp = FontPreview('noto.ttf')
fp.save('/tmp/fp.png')  # White backgroung with 'a b c d e f' letters 64pt in black
```

Banner example:
```python
from fontpreview import FontBanner

fb = FontBanner('noto.ttf', 'landscape', bg_color=(153, 153, 255), mode='fontname')
fb.save('/tmp/fb.png')  # Light purple landscape backgroung with 'Noto' font name in black
```

Logo example:
```python
from fontpreview import FontLogo

fl = FontLogo('noto.ttf', 'Fp')
fl.save('/tmp/fl.png')  # White logo with 'Fp' letters 64pt in black
```

Font wall example:
```python
from fontpreview import FontBanner, FontWall

fb = FontBanner('noto.ttf', 'landscape' , mode='fontname')
fb2 = FontBanner('noto.ttf', 'landscape' , mode='alpha')
fb3 = FontBanner('noto.ttf', 'landscape' , mode='letter')
fb4 = FontBanner('noto.ttf', 'landscape' , mode='paragraph')
fw = FontWall([fb,fb2,fb3,fb4])
fw.save('/tmp/fw.png')  # White landscape backgroung with 'Noto' font name, letter and number, all letter and paragraph in black
```

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

Special thanks go to my wife, who understood the hours of absence for this development. 
Thanks to my children, for the daily inspiration they give me and to make me realize, that life must be simple.

Thanks Python!
