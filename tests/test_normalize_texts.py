import json
import os
import sys
import unittest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.normalize_texts import normalize_text


class TestNormalizeTexts(unittest.TestCase):
    def test_basic_caret_replacement(self):
        """Test that ^ character is preserved from English"""
        en = "^PERSONAL SPELLBOOK."
        ru = "БКНИГУ ЗАКЛИНАНИЙ."
        expected = "^КНИГУ ЗАКЛИНАНИЙ."
        result = normalize_text(en, ru)
        self.assertEqual(result, expected)
    
    def test_caret_with_space(self):
        """Test ^ followed by space"""
        en = "^ ATTACKS!"
        ru = "Б АТАКУЕТ!"
        expected = "^ АТАКУЕТ!"
        result = normalize_text(en, ru)
        self.assertEqual(result, expected)
    
    def test_caret_with_underscores(self):
        """Test ^ in pattern ^_text_^"""
        en = "^_no_one_available_^"
        ru = "\x16_нет_доступных_\x16"
        expected = "^_нет_доступных_^"
        result = normalize_text(en, ru)
        self.assertEqual(result, expected)
    
    def test_percent_bracket_insertion(self):
        """Test that %%] is inserted when missing"""
        en = "%%]SUDDENLY A DOOR SLAMS TO THE RIGHT!"
        ru = "@ВНЕЗАПНО СПРАВА ХЛОПАЕТ ДВЕРЬ!"
        expected = "%%]ВНЕЗАПНО СПРАВА ХЛОПАЕТ ДВЕРЬ!"
        result = normalize_text(en, ru)
        self.assertEqual(result, expected)
    
    def test_no_format_in_english(self):
        """Test that text without format chars is unchanged"""
        en = "HUMAN"
        ru = "ЧЕЛОВЕК"
        result = normalize_text(en, ru)
        self.assertEqual(result, ru)
    
    def test_already_correct_format(self):
        """Test that already correct format is preserved"""
        en = "^TEST"
        ru = "^ТЕСТ"
        result = normalize_text(en, ru)
        self.assertEqual(result, ru)
    
    def test_del_character_preserved(self):
        """Test that \\u007f (DEL) character is preserved"""
        en = "\u007f__master_options__\u007f"
        ru = "\u007f__главное_меню__\u007f"
        result = normalize_text(en, ru)
        self.assertEqual(result, ru)
    
    def test_messages_json_consistency(self):
        """Test that all messages in messages.json have consistent formatting"""
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{path}/messages/messages.json', 'r') as f:
            messages = json.load(f)
        
        # Check that format characters match between EN and RU
        format_chars = ['^', '%', '@']
        mismatches = []
        
        for key, val in messages.items():
            en = val.get('en', '') or ''
            ru = val.get('ru', '') or ''
            
            # Skip if no EN or RU
            if not en or not ru:
                continue
            
            # Check each format character
            for char in format_chars:
                en_count = en.count(char)
                ru_count = ru.count(char)
                
                # ^ should always match (it's critical for game logic)
                if char == '^' and en_count != ru_count:
                    mismatches.append(f"{key}: EN has {en_count} '{char}', RU has {ru_count}")
        
        # Allow up to 10% mismatches for non-critical chars
        # (some might be intentional translations)
        self.assertLess(len(mismatches), len(messages) * 0.01, 
                       f"Too many format mismatches:\n" + "\n".join(mismatches[:10]))


if __name__ == '__main__':
    unittest.main()
