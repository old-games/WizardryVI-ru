import os
import unittest

from PIL import Image, ImageChops

import tools.ega
import tools.font
import tools.portrait


class TestEGA(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (320, 200, 'DRAGONSC.EGA'),
            (320, 200, 'GRAVEYRD.EGA'),
            (320, 200, 'TITLEPAG.EGA'),
        ]
        for w, h, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                picture = tools.ega.decode(data, w, h)
                expected_path = os.path.join(path, 'ega', fname + '.png')
                self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                expected = Image.open(expected_path)
                expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                diff = ImageChops.difference(picture, expected)
                bbox = diff.getbbox()
                self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")

    def test_read_fonts(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (8, 8, 8, tools.ega.decode_one_bit, 'WFONT0.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT1.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT2.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT3.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT4.EGA'),
        ]
        for size, w, h, decode_func, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index, symbol in enumerate(symbols):
                    with self.subTest(symbol=symbol_index):
                        picture = decode_func(symbol, w, h)
                        expected_path = os.path.join(path, 'ega', 'fonts', f'{fname}.{symbol_index:03d}.png')
                        self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")

    def test_read_fonts2(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (8, 8, 8, tools.ega.decode_one_bit, 'WFONT0.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT1.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT2.EGA'),
            (32, 8, 8, tools.ega.decode, 'WFONT3.EGA'),
        ]
        for size, w, h, decode_func, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'new', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index, symbol in enumerate(symbols):
                    with self.subTest(symbol=symbol_index):
                        picture = decode_func(symbol, w, h)
                        expected_path = os.path.join(path, 'new', f'{fname}.{symbol_index:03d}.png')
                        picture.resize((picture.width*10, picture.height*10), resample=0).save(expected_path)

    def test_write_fonts(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pictures = [
            (8, 8, 8, tools.ega.decode_one_bit, tools.ega.encode_one_bit, 'WFONT0.EGA'),
            (32, 8, 8, tools.ega.decode, tools.ega.encode, 'WFONT1.EGA'),
            (32, 8, 8, tools.ega.decode, tools.ega.encode, 'WFONT2.EGA'),
            (32, 8, 8, tools.ega.decode, tools.ega.encode, 'WFONT3.EGA'),
            (32, 8, 8, tools.ega.decode, tools.ega.encode, 'WFONT4.EGA'),
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
            (32, 8, 8, 9, 'WPORT1.EGA'),
            (32, 8, 8, 9, 'WPORT2.EGA'),
            (32, 8, 8, 9, 'WPORT3.EGA'),
        ]
        for size, w, h, block_size, fname in pictures:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                symbols = tools.font.decode(data, size)
                for symbol_index in range(len(symbols)//block_size):
                    with self.subTest(symbol=symbol_index):
                        fragments = [tools.ega.decode(symbols[symbol_index*block_size + i], w, h) for i in range(block_size)]
                        picture = tools.portrait.merge(fragments)
                        expected_path = os.path.join(path, 'ega', 'portraits', f'{fname}.{symbol_index:02d}.png')
                        self.assertTrue(os.path.exists(expected_path), f"Expected image {expected_path} does not exist")
                        expected = Image.open(expected_path)
                        expected = expected.resize((expected.width//10, expected.height//10), resample=0)
                        diff = ImageChops.difference(picture, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f"Decoded image for {fname} does not match expected image")
                assert set(b''.join(symbols[len(symbols)//block_size*block_size:])) == {0}

    def test_read_maze(self):
        raise NotImplementedError("No maze images to test")
        (320, 200, 'MAZEDATA.EGA'),
