import json
import os
import unittest


class TestMessages(unittest.TestCase):
    def test_messages(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{path}/messages/messages.json', 'r') as f:
            messages = json.loads(f.read())
        self.assertIsInstance(messages, dict)
        self.assertGreater(len(messages), 0)
        for k, v in messages.items():
            with self.subTest(key=k):
                self.assertIsInstance(k, str)
                self.assertRegex(k, r'^\d{5}$')
                self.assertIsInstance(v, dict)
                self.assertIn('ru', v)
                self.assertIn('en', v)
                self.assertIsInstance(v['ru'], str)
                self.assertTrue(isinstance(v['en'], str) or v['en'] is None)
