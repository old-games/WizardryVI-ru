import os
import unittest

import tools.rle


class TestRLE(unittest.TestCase):
    def test_decompress(self):
        compressed = bytes([0xfe, 0x01, 0x02, 0x03, 0x04, 0x03, 0x06, 0x07, 0x08])
        uncompressed = tools.rle.decompress(compressed)
        expected = bytes([1, 1, 3, 4, 6, 7, 8])
        self.assertEqual(uncompressed, expected)

    def test_decompress_with_padding(self):
        for pad in (0x80, 0x7f):
            with self.subTest(pad=pad):
                compressed = bytes([0x01, 0x02] * 0x7fe + [0x02, 0x01, 0x02] + [pad] + [0x01, 0x42])
                uncompressed = tools.rle.decompress(compressed)
                expected = bytes([0x02] * 0x7fe + [1, 2] + [0x42])
                self.assertEqual(uncompressed, expected)

    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for fname in os.listdir(os.path.join(path, 'unpacked')):
            if not fname.upper().endswith('.PIC'):
                continue
            with open(os.path.join(path, 'unpacked', fname), 'rb') as f:
                compressed = f.read()
            with self.subTest(file=fname):
                uncompressed = tools.rle.decompress(compressed)
                self.assertIsInstance(uncompressed, bytes)
                self.assertGreater(len(uncompressed), 0)
