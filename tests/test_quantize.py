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
        for format_dir, format_extension in cls.formats:
            name_directory_parts = os.path.split(name)
            if len(name_directory_parts) > 1:
                prefix = name_directory_parts[:-1]
                name = name_directory_parts[-1]
            else:
                prefix = []
            name_parts = name.split('.')
            assert len(name_parts) <= 2, f'Expected name to have at most one dot, got `{name}`.'
            if len(name_parts) == 2:
                name, index = name_parts
                assert index.isdigit()
            else:
                name = name_parts[0]
                index = None
            files = os.listdir(os.path.join(path, format_dir, *prefix))
            for file_name in files:
                file_path = os.path.join(path, format_dir, *prefix, file_name)
                if os.path.isfile(file_path):
                    basename, extension = os.path.splitext(file_name)
                    assert extension == '.png', f'Expected PNG file, got `{file_name}`.'
                    parts = basename.split('.')
                    assert len(parts) in {2, 3, 4}, f'Unexpected file name format for `{file_name}`.'
                    assert parts[1] == format_extension, f'Expected file name to contain format extension `{format_extension}`, got `{file_name}`.'
                    if len(parts) > 2 and parts[2].isdigit():
                        index_found = parts[2]
                        parts = parts[:2] + parts[3:]
                    else:
                        index_found = None
                    name_found = parts[0]
                    if (name, index) == (name_found, index_found):
                        language = parts[2] if len(parts) > 2 else None
                        languages.add(language)
        return languages

    def _get_paths(self, name, language, path):
        paths = {}
        name_parts = name.split('.')
        assert len(name_parts) in {1, 2}, f'Expected name to have at most one dot, got `{name}`.'
        if len(name_parts) == 2:
            name, index = name_parts
            assert index.isdigit()
            index = f'.{index}'
        else:
            name = name_parts[0]
            index = ''
        for format_dir, format_ext in self.formats:
            file_name = f'{name}.{format_ext}{index}'
            if language:
                file_name += f'.{language}'
            file_name += '.png'
            file_path = os.path.join(path, format_dir, file_name)
            self.assertTrue(os.path.isfile(file_path), f'Expected file `{file_path}` does not exist.')
            paths[format_dir] = file_path
        return paths

    def test_ega_and_tandy_match_and_cga_exists(self):
        names = (
            ('DRAGONSC', None, None),
            ('GRAVEYRD', None, None),
            ('TITLEPAG', None, None),
            ('maze/MAZEDATA', 3, 153),
            ('portraits/WPORT1', 2, 14),
            ('portraits/WPORT2', 2, 14),
            ('portraits/WPORT3', 2, 14),
            #('fonts/WFONT0', 3, 128), # FIXME fonts have additional codes for CP-866.
            #('fonts/WFONT1', 3, 128),
            #('fonts/WFONT2', 3, 128),
            #('fonts/WFONT3', 3, 128), # FIXME fonts have additional codes for CP-866.
            #('fonts/WFONT4', 3, 128),
        )
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for name, number_size, max_number in names:
            if max_number is None:
                numbers = [None]
            else:
                numbers = list(range(max_number))
            for index in numbers:
                with self.subTest(name=name, index=index):
                    if index is not None:
                        name_with_index = f'{name}.{str(index).zfill(number_size)}'
                    else:
                        name_with_index = name
                    languages = self._get_languages(name_with_index, path)
                    if languages == set():
                        print(f'Testing `{name_with_index}` with languages: {languages}')
                    for language in sorted(languages, key=lambda x: x or 'en'):
                        with self.subTest(language=language):
                            paths = self._get_paths(name_with_index, language, path)

                            with open(paths['ega'], 'rb') as f:
                                ega_data = f.read()
                            with open(paths['tandy'], 'rb') as f:
                                tandy_data = f.read()
                            if language is None and name == 'fonts/WFONT4' and index == 103:
                                # Expected fail.
                                continue
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
