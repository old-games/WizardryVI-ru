import collections
import os
import unittest

import PIL.Image

import tools.rle
import tools.picture


class TestPicture(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        all_pictures = collections.defaultdict(list)
        pictures_dir = os.path.join(path, 'pictures')
        for fname in sorted(os.listdir(pictures_dir)):
            if fname.endswith('.PIC.png'):
                base, _, _ = fname.rsplit('.', maxsplit=2)
                assert '.' in base
                name, idx = base.rsplit('.', 1)
                idx = int(idx)
                all_pictures[f'{name}.PIC'].append(fname)
        for fname in os.listdir(os.path.join(path, 'original')):
            if not fname.upper().endswith('.PIC'):
                continue
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    compressed = f.read()
                expected_pictures = []
                uncompressed = tools.rle.decompress(compressed)
                pictures = tools.picture.decode(uncompressed)
                self.assertIsInstance(pictures, list)
                self.assertGreater(len(pictures), 0)
                self.assertIn(fname, all_pictures)
                for pic_fname in all_pictures[fname]:
                    with PIL.Image.open(os.path.join(pictures_dir, pic_fname)) as img:
                        img = img.resize((img.width // 10, img.height // 10), resample=0)
                        expected_pictures.append((img.size, img.mode, list(img.getdata())))
                self.assertEqual(len(pictures), len(expected_pictures))
                for img, (size, mode, data) in zip(pictures, expected_pictures):
                    self.assertIsInstance(img, tools.picture.PIL.Image.Image)
                    self.assertEqual(len(img.getdata()), len(data))
                    self.assertEqual(img.size, size)
                    self.assertEqual(img.mode, mode)
                    self.assertEqual(list(img.getdata()), data)

    def test_write_roundtrip_uncompressed(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        originals_dir = os.path.join(path, 'original')
        candidates = [f for f in os.listdir(originals_dir) if f.upper().endswith('.PIC')]
        self.assertGreater(len(candidates), 0, 'No .PIC files found under original/.')
        for fname in candidates:
            with self.subTest(file=fname):
                with open(os.path.join(originals_dir, fname), 'rb') as f:
                    compressed = f.read()
                uncompressed = tools.rle.decompress(compressed)
                pictures = tools.picture.decode(uncompressed)
                reencoded = tools.picture.encode(pictures, warn_on_non_palette=False)
                if fname == 'CREDITS.PIC':
                    assert set(uncompressed[-0x5e0:]) == {0}
                    uncompressed = uncompressed[:-0x5e0]
                self.assertEqual(reencoded, uncompressed, f'PIC re-encode mismatch for {fname}.')

    def test_write_warns_on_non_palette(self):
        img = PIL.Image.new('RGBA', (8, 8), (1, 2, 3, 255))
        with self.assertWarns(RuntimeWarning):
            data = tools.picture.encode([img], warn_on_non_palette=True)
        self.assertIsInstance(data, bytes)
