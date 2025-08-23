import os
import unittest

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
                #picture = picture.resize((picture.width*10, picture.height*10), resample=0)
                #picture.save(os.path.join(path, 'cga', fname + '.png'))
                # FIXME
