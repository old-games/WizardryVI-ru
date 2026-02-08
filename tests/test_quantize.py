import os
import unittest

import PIL.Image
import PIL.ImageChops

import tools.quantize
import tools.tenfold


class TestQuantize(unittest.TestCase):
    formats = (
        ('ega', 'EGA'),
        ('cga', 'CGA'),
        ('tandy', 'T16'),
    )

    @classmethod
    def _get_languages(cls, name, path):
        languages = set()
        for format_dir, _ in cls.formats:
            files = os.listdir(os.path.join(path, format_dir))
            for file_name in files:
                file_path = os.path.join(path, format_dir, file_name)
                if os.path.isfile(file_path):
                    parts = os.path.splitext(file_name)[0].split('.')
                    if parts[0] == name:
                        language = parts[2] if len(parts) > 2 else None
                        languages.add(language)
        return languages

    def _get_paths(self, name, language, path):
        paths = {}
        for format_dir, format_ext in self.formats:
            file_name = f'{name}.{format_ext}'
            if language:
                file_name += f'.{language}'
            file_name += '.png'
            file_path = os.path.join(path, format_dir, file_name)
            self.assertTrue(os.path.isfile(file_path), f'Expected file `{file_path}` does not exist.')
            paths[format_dir] = file_path
        return paths

    def test_tandy_matches(self):
        names = (
            'DRAGONSC',
            'GRAVEYRD',
            'TITLEPAG',
        )
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for name in names:
            with self.subTest(name=name):
                languages = self._get_languages(name, path)
                for language in sorted(languages, key=lambda x: x or 'en'):
                    with self.subTest(language=language):
                        paths = self._get_paths(name, language, path)

                        with open(paths['ega'], 'rb') as f:
                            ega_data = f.read()
                        with open(paths['tandy'], 'rb') as f:
                            tandy_data = f.read()
                        self.assertEqual(ega_data, tandy_data, 'EGA and TANDY files differ, expected them to be identical.')

    def test_cga_matches(self):
        names = (
            #'DRAGONSC',
            #'GRAVEYRD',
            'TITLEPAG',
        )
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for name in names:
            with self.subTest(name=name):
                languages = self._get_languages(name, path)
                for language in sorted(languages, key=lambda x: x or 'en'):
                    with self.subTest(language=language):
                        paths = self._get_paths(name, language, path)

                        image_sixteen = tools.tenfold.decode(PIL.Image.open(paths['ega']))
                        image_four = tools.tenfold.decode(PIL.Image.open(paths['cga']))
                        quantized = tools.quantize.ega_to_cga(image_sixteen)

                        diff = PIL.ImageChops.difference(quantized, image_four)
                        bbox = diff.getbbox()
                        self.assertIsNone(bbox, 'Quantized EGA does not match CGA.')
