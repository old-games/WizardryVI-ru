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
    def test_read_maze(self):
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
