import os
import unittest

from PIL import Image, ImageChops

import tools.cga


class TestCGA(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = ['DRAGONSC.CGA', 'GRAVEYRD.CGA', 'TITLEPAG.CGA']
        for fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'unpacked', fname), 'rb') as f:
                    data = f.read()
                picture = tools.cga.decode(data, 320, 200)
                expected_path = os.path.join(path, 'cga', fname + '.png')
                self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                expected = Image.open(expected_path)
                expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                diff = ImageChops.difference(picture, expected)
                bbox = diff.getbbox()
                self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image.")
