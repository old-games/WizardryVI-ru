import os
import unittest

from PIL import Image, ImageChops

import tools.font
import tools.portrait
import tools.tandy


class TestTandy(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = ['DRAGONSC.T16', 'GRAVEYRD.T16', 'TITLEPAG.T16']
        for fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                picture = tools.tandy.decode(data, 320, 200)
                expected_path = os.path.join(path, 'tandy', fname + '.png')
                self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                expected = Image.open(expected_path)
                expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                diff = ImageChops.difference(picture, expected)
                bbox = diff.getbbox()
                self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")

    def test_read_fonts(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (32, 8, 8, tools.tandy.decode_one_bit, 'WFONT0.T16'),
            (32, 8, 8, tools.tandy.decode, 'WFONT1.T16'),
            (32, 8, 8, tools.tandy.decode, 'WFONT2.T16'),
            (32, 8, 8, tools.tandy.decode, 'WFONT3.T16'),
            (32, 8, 8, tools.tandy.decode, 'WFONT4.T16'),
        ]
        for size, w, h, decode_func, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index, symbol in enumerate(symbols):
                    with self.subTest(symbol=symbol_index):
                        picture = decode_func(symbol, w, h)
                        expected_path = os.path.join(path, 'tandy', 'fonts', f'{fname}.{symbol_index:03d}.png')
                        self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")

    def test_read_portraits(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (32, 8, 8, 9, 'WPORT1.T16'),
            (32, 8, 8, 9, 'WPORT2.T16'),
            (32, 8, 8, 9, 'WPORT3.T16'),
        ]
        for size, w, h, block_size, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index in range(len(symbols)//block_size):
                    with self.subTest(symbol=symbol_index):
                        fragments = [tools.tandy.decode(symbols[symbol_index*block_size + i], w, h) for i in range(block_size)]
                        picture = tools.portrait.merge(fragments)
                        expected_path = os.path.join(path, 'tandy', 'portraits', f'{fname}.{symbol_index:02d}.png')
                        self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")
                assert set(b''.join(symbols[len(symbols)//block_size*block_size:])) == {0}

    def test_read_maze(self):
        raise NotImplementedError("No maze images to test")
        (320, 200, 'MAZEDATA.T16'),
