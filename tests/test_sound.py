import os
import unittest
import wave

import tools.sound


class TestSound(unittest.TestCase):
    def test_read(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sounds = [x for x in os.listdir(os.path.join(path, 'original')) if x.upper().endswith('.SND')]
        for fname in sounds:
            with self.subTest(file=fname):
                with open(os.path.join(path, 'original', fname), 'rb') as f:
                    data = f.read()
                sound = tools.sound.decode(data)
                expected_path = os.path.join(path, 'sounds', fname + '.wav')
                with wave.open(expected_path, 'rb') as wf:
                    self.assertEqual(sound, wf.readframes(wf.getnframes()))
