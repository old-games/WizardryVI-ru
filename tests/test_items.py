import json
import os
import unittest


class TestItems(unittest.TestCase):
    def test_items(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{path}/items/items.json', 'r') as f:
            items = json.loads(f.read())
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)
        for i, item in enumerate(items):
            with self.subTest(index=i):
                self.assertIsInstance(item, dict)
                self.assertIn('id', item)
                self.assertIn('name', item)
                self.assertIn('raw', item)
                self.assertIsInstance(item['id'], int)
                self.assertIsInstance(item['name'], dict)
                self.assertIn('en', item['name'])
                self.assertIn('ru', item['name'])
                self.assertIsInstance(item['name']['en'], str)
                self.assertIsInstance(item['name']['ru'], str)
                self.assertIsInstance(item['raw'], str)
                self.assertEqual(len(item['raw']), 0x3a * 2)
                self.assertLess(len(item['name']['ru']), 16)
                self.assertLess(len(item['name']['en']), 16)
