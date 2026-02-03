import os
import unittest

from PIL import Image, ImageChops

import tools.cga
import tools.font
import tools.portrait


class TestCGA(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = ['DRAGONSC.CGA', 'GRAVEYRD.CGA', 'TITLEPAG.CGA']
        for fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                picture = tools.cga.decode(data, 320, 200)
                expected_path = os.path.join(path, 'cga', fname + '.png')
                self.assertTrue(os.path.exists(expected_path), f'Expected image `{expected_path}` does not exist.')
                expected = Image.open(expected_path)
                expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                diff = ImageChops.difference(picture, expected)
                bbox = diff.getbbox()
                self.assertIsNone(bbox, f'Decoded image for `{fname}` does not match expected image.')

    def test_read_fonts(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (16, 8, 8, tools.cga.decode_one_bit, 'WFONT0.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, 'WFONT1.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, 'WFONT2.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, 'WFONT3.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, 'WFONT4.CGA'),
        ]
        for size, w, h, decode_func, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index, symbol in enumerate(symbols):
                    with self.subTest(symbol=symbol_index):
                        picture = decode_func(symbol, w, h)
                        expected_path = os.path.join(path, 'cga', 'fonts', f'{fname}.{symbol_index:03d}.png')
                        self.assertTrue(os.path.exists(expected_path), f'Expected image `{expected_path}` does not exist.')
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f'Decoded image for `{fname}` does not match expected image.')

    def test_write_fonts(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (16, 8, 8, tools.cga.decode_one_bit, tools.cga.encode_one_bit, 'WFONT0.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, tools.cga.encode_without_interleaving, 'WFONT1.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, tools.cga.encode_without_interleaving, 'WFONT2.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, tools.cga.encode_without_interleaving, 'WFONT3.CGA'),
            (16, 8, 8, tools.cga.decode_without_interleaving, tools.cga.encode_without_interleaving, 'WFONT4.CGA'),
        ]
        for size, w, h, decode_func, encode_func, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    original_data = f.read()
                symbols = tools.font.decode(original_data, size)
                for symbol_index, symbol in enumerate(symbols):
                    with self.subTest(symbol=symbol_index):
                        encoded_symbol = encode_func(decode_func(symbol, w, h))
                        self.assertEqual(encoded_symbol, symbol, f'Encoded symbol {symbol_index} for `{fname}` does not match original.')
                encoded_data = b''.join([encode_func(decode_func(symbol, w, h)) for symbol in symbols])
                self.assertEqual(encoded_data, original_data, f'Encoded data for `{fname}` does not match original.')
                reassembled = tools.font.encode(symbols)
                self.assertEqual(reassembled, original_data, f'Encoded font data for `{fname}` does not match original file.')

    def test_read_portraits(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (16, 8, 8, 9, 'WPORT1.CGA'),
            (16, 8, 8, 9, 'WPORT2.CGA'),
            (16, 8, 8, 9, 'WPORT3.CGA'),
        ]
        for size, w, h, block_size, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index in range(len(symbols)//block_size):
                    with self.subTest(symbol=symbol_index):
                        fragments = [tools.cga.decode_without_interleaving(symbols[symbol_index*block_size + i], w, h) for i in range(block_size)]
                        picture = tools.portrait.merge(fragments)
                        expected_path = os.path.join(path, 'cga', 'portraits', f'{fname}.{symbol_index:02d}.png')
                        self.assertTrue(os.path.exists(expected_path), f'Expected image {expected_path} does not exist.')
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f'Decoded image for {fname} does not match expected image.')
                assert set(b''.join(symbols[len(symbols)//block_size*block_size:])) == {0}

    @unittest.skip('TODO')
    def test_read_maze(self):
        raise NotImplementedError('No maze images to test.')
        (320, 200, 'MAZEDATA.CGA'),
