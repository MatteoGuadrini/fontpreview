# Release notes

## 1.2.0
Dec 12, 2020

- Additions show method on *FontPreview*, *FontWall*, *FontPage* class
- Additions _FontBooklet_ class
- Fix FontPageTemplate *\__str\__* method
- Fix message raises on set_header/logo/body/footer method on _FontPage_ class

## 1.1.0
Dec 12, 2020

- Additions declaration mode for *FontPage* class
- Additions *test_hex_color* method on TestFontPreview class
- Additions *test_hex_color* method on TestFontPreview class
- Additions *test_declarative_object* method on TestFontPreview class
- Additions *test_other_color_system* method on TestFontPreview class
- Fix TestFontPreview.test_font_size method and FontPage.__compose method
- Fix test_text_position method on TestFontPreview class

## 1.0.0
Dec 5, 2020

- *fontpreview* python package is available.
- *fp* command line tool is available.
- *FontPreview* class represents a preview object of a given font.
- *FontBanner* class represents a preview banner object of a given font. Based on *FontPreview* class.
- *FontLogo* class represents a logo object of a given font. Based on *FontPreview* class.
- *FontWall* class represents a wall of preview fonts object.
- *FontPage* class represents a page of preview fonts object.
- *FontPageTemplate* class represents a template for *FontPage* class.
- Documentation has been created