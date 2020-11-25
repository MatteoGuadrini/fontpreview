import unittest
import os
from fontpreview import FontPreview, FontBanner, FontLogo, FontWall, FontPage, FontPageTemplate

# Enter the file font to test and check exists
font = input('Enter path of font file to test: ')
if not os.path.exists(font):
    raise OSError("file font {0} doesn't exists".format(font))


class TestFontPreview(unittest.TestCase):
    def test_create_instance(self):
        fp, fb, fl = FontPreview(font), FontBanner(font), FontLogo(font, 'Fl')
        fw, fpage, fpage_t = FontWall([fb]), FontPage(), FontPageTemplate(3508)
        # test if instance has been created
        self.assertIsInstance(fp, FontPreview)
        self.assertIsInstance(fb, FontBanner)
        self.assertIsInstance(fl, FontLogo)
        self.assertIsInstance(fw, FontWall)
        self.assertIsInstance(fpage, FontPage)
        self.assertIsInstance(fpage_t, FontPageTemplate)


if __name__ == '__main__':
    unittest.main()
