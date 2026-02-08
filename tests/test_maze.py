import os
import unittest

import PIL.Image
import PIL.ImageChops

import tools.cga
import tools.ega
import tools.maze
import tools.tandy
import tools.tenfold


class TestMaze(unittest.TestCase):
    def test_decode(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for name, directory, decode in (
            ('MAZEDATA.EGA', 'ega', tools.ega.decode),
            ('MAZEDATA.CGA', 'cga', tools.cga.decode_without_interleaving),
            ('MAZEDATA.T16', 'tandy', tools.tandy.decode),
        ):
            with self.subTest(name=name):
                with open(os.path.join(path, 'original', name), 'rb') as f:
                    data = f.read()
                data, _ = tools.maze.decode(data)
                for index, (w, h, payload) in enumerate(data):
                    with self.subTest(index=index):
                        image = decode(payload, w, h)
                        with open(os.path.join(path, directory, 'maze', f'{name}.{index:03d}.png'), 'rb') as f:
                            expected = tools.tenfold.decode(PIL.Image.open(f))
                        diff = PIL.ImageChops.difference(image, expected)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, f'Maze image does not match expected image.')

    def test_encode(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for name, directory, encode in (
            ('MAZEDATA.EGA', 'ega', tools.ega.encode),
            ('MAZEDATA.CGA', 'cga', tools.cga.encode_without_interleaving),
            ('MAZEDATA.T16', 'tandy', tools.tandy.encode),
        ):
            with self.subTest(name=name):
                with open(os.path.join(path, 'original', name), 'rb') as f:
                    original_data = f.read()
                _, objects = tools.maze.decode(original_data)
                all_pictures = []
                for picture_name in sorted(os.listdir(os.path.join(path, directory, 'maze'))):
                    assert picture_name.endswith('.png')
                    parts = os.path.splitext(picture_name)[0].split('.')
                    assert len(parts) in {3, 4}
                    if len(parts) == 3:
                        base_name, format_name, index = parts
                        assert index.isdigit()
                        assert f'{base_name}.{format_name}' == name
                        with PIL.Image.open(os.path.join(path, directory, 'maze', picture_name)) as image:
                            data = tools.tenfold.decode(image)
                            all_pictures.append((data.size[0], data.size[1], encode(data)))
                encoded = tools.maze.encode(all_pictures, objects) # TODO read that from JSON
                self.assertEqual(encoded, original_data, 'Encoded maze data does not match original data.')
