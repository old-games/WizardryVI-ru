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
        for fname in os.listdir(os.path.join(path, 'original')):
            if not fname.upper().endswith('.PIC'):
                continue
            with open(os.path.join(path, 'original', fname), 'rb') as f:
                compressed = f.read()
            with self.subTest(file=fname):
                uncompressed = tools.rle.decompress(compressed)
                self.assertIsInstance(uncompressed, bytes)
                self.assertGreater(len(uncompressed), 0)

    def test_decompress_compress_roundtrip(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for fname in os.listdir(os.path.join(path, 'original')):
            if not fname.upper().endswith('.PIC'):
                continue
            with open(os.path.join(path, 'original', fname), 'rb') as f:
                compressed = f.read()
            with self.subTest(file=fname):
                uncompressed = tools.rle.decompress(compressed)
                recompressed = tools.rle.compress(uncompressed)
                if recompressed != tools.rle.normalize_compressed(compressed, is_original=True):
                    uncompressed_debug = tools.rle.decompress_debug(tools.rle.normalize_compressed(compressed, is_original=True))
                    recompressed_debug = tools.rle.decompress_debug(recompressed)
                    def describe(l):
                        result = []
                        i = 0
                        j = 0
                        for entry_type, data in l:
                            #result.append((i, j, entry_type.name, len(data), data[:8].hex().upper() + ('...' if len(data) > 8 else '')))
                            result.append((i, j, entry_type.name, len(data), data.hex().upper()))
                            i += len(data)
                            match entry_type:
                                case tools.rle.EntryType.PADDING:
                                    j += 1
                                case tools.rle.EntryType.LITERAL:
                                    j += len(data)
                                case tools.rle.EntryType.RLE:
                                    j += 1
                            j += 1
                        return result
                    uncompressed_debug = describe(uncompressed_debug)
                    recompressed_debug = describe(recompressed_debug)
                    #for i in range(min(len(uncompressed_debug), len(recompressed_debug))):
                    #    self.assertEqual(uncompressed_debug[i], recompressed_debug[i], f'RLE decompress debug mismatch for {fname} at entry {i} (out of {len(uncompressed_debug)}).')
                    #self.assertEqual(uncompressed_debug[-50:], recompressed_debug[-50:], f'RLE decompress debug mismatch for {fname}.')
                    with open(f'recompressed_{fname}.diff', 'w') as diff_f:
                        import difflib
                        diff = difflib.unified_diff(
                            [f'{i}\t{j}\t{etype}\t{length}\t{data}\n' for (i, j, etype, length, data) in uncompressed_debug],
                            [f'{i}\t{j}\t{etype}\t{length}\t{data}\n' for (i, j, etype, length, data) in recompressed_debug],
                            fromfile='original',
                            tofile='recompressed',
                            n=100,
                        )
                        diff_f.writelines(diff)
                    self.assertEqual(recompressed_debug, uncompressed_debug, f'RLE decompress debug mismatch for {fname}.')

                with self.subTest(type='compressed'):
                    if recompressed != tools.rle.normalize_compressed(compressed, is_original=True):
                        self.assertEqual(recompressed, compressed, f'RLE re-compress mismatch for {fname}.')

                with self.subTest(type='uncompressed'):
                    uncompressed_twice = tools.rle.decompress(recompressed)
                    self.assertEqual(uncompressed, uncompressed_twice, f'RLE re-compress uncompressed mismatch for {fname}.')
