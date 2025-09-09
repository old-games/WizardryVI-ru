import json
import os
import unittest

class TestMonsters(unittest.TestCase):
    def test_monsters(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{path}/monsters/monsters.json', 'r') as f:
            monsters = json.loads(f.read())
        self.assertIsInstance(monsters, list)
        self.assertGreater(len(monsters), 0)
        for i, monster in enumerate(monsters):
            with self.subTest(index=i):
                self.assertIsInstance(monster, dict)
                self.assertIn('id', monster)
                self.assertIsInstance(monster['id'], int)
                self.assertIn('raw', monster)
                self.assertIsInstance(monster['raw'], str)
                self.assertEqual(len(monster['raw']), 0x9e * 2)
                for name_field in ['name-singular', 'name-plural', 'hidden-name-singular', 'hidden-name-plural']:
                    with self.subTest(field=name_field):
                        self.assertIn(name_field, monster)
                        self.assertIsInstance(monster[name_field], dict)
                        self.assertIn('ru', monster[name_field])
                        self.assertIsInstance(monster[name_field]['ru'], str)
                        self.assertIn('en', monster[name_field])
                        self.assertIsInstance(monster[name_field]['en'], str)
                        self.assertLess(len(monster[name_field]['ru']), 16)
                        self.assertLess(len(monster[name_field]['en']), 16)
