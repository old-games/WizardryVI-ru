import json
import os
import unittest


class TestNpcs(unittest.TestCase):
    def test_npcs(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{path}/npcs/npcs.json', 'r') as f:
            npcs = json.loads(f.read())
        self.assertIsInstance(npcs, list)
        self.assertGreater(len(npcs), 0)
        for i, npc in enumerate(npcs):
            with self.subTest(index=i):
                self.assertIsInstance(npc, dict)
                self.assertIn('id', npc)
                self.assertIsInstance(npc['id'], int)
                self.assertIn('name', npc)
                self.assertIsInstance(npc['name'], dict)
                self.assertIn('en', npc['name'])
                self.assertIn('ru', npc['name'])
                self.assertIsInstance(npc['name']['en'], str)
                self.assertIsInstance(npc['name']['ru'], str)
                self.assertIn('raw', npc)
                self.assertIsInstance(npc['raw'], str)
                self.assertEqual(len(npc['raw']), 0x7e * 2)
                self.assertLess(len(npc['name']['ru']), 16)
                self.assertLess(len(npc['name']['en']), 16)
