import os
import unittest

import PIL.Image
import PIL.ImageChops

import tools.tenfold


class TestTenfold(unittest.TestCase):
    def test_correct(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        directories = [os.path.join(path, 'pictures')]
        formats = ('ega', 'cga', 'tandy')
        for format in formats:
            directories.append(os.path.join(path, format))
            directories.append(os.path.join(path, format, 'fonts'))
            directories.append(os.path.join(path, format, 'portraits'))
            directories.append(os.path.join(path, format, 'maze'))
        for directory in directories:
            with self.subTest(directory=directory):
                for fname in os.listdir(directory):
                    if os.path.splitext(fname)[1] == '.png':
                        with self.subTest(name=fname):
                            image = PIL.Image.open(os.path.join(directory, fname))
                            try:
                                decoded = tools.tenfold.decode(image)
                            except Exception as e:
                                self.fail(f'Failed to decode `{fname}` from `{directory}`: {e}.')

                            encoded = tools.tenfold.encode(decoded)
                            diff = PIL.ImageChops.difference(encoded, image)
                            bbox = diff.getbbox()
                            self.assertIsNone(bbox, f'Encoded image for `{fname}` in `{directory}` does not match the original.')
