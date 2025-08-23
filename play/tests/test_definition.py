import unittest

import definition


class TestDefinition(unittest.TestCase):
    def test_classes_experience(self):
        for character_class in definition.Class._member_map_.values():
            with self.subTest(character_class=character_class):
                for level in (1, 20):
                    with self.subTest(level=level):
                        definition.get_level_experience(character_class, level)

    def test_classes_skills(self):
        for character_class in definition.Class._member_map_.values():
            with self.subTest(character_class=character_class):
                for skill_type in definition.SkillType._member_map_.values():
                    with self.subTest(skill_type=skill_type):
                        self.assertGreater(len(definition.get_class_skills(character_class, skill_types={skill_type})), 0)

    def test_races_parameters(self):
        for race in definition.Race._member_map_.values():
            with self.subTest(race=race):
                parameters = definition.get_race_parameters(race)
                for parameter in definition.Parameter._member_map_.values():
                    with self.subTest(parameter=parameter):
                        self.assertIn(parameter, parameters)
                        self.assertIsInstance(parameters[parameter], int)
                        self.assertGreater(parameters[parameter], 0)

    def test_classes_requirements(self):
        for character_class in definition.Class._member_map_.values():
            with self.subTest(character_class=character_class):
                requirements = definition.get_class_requirements(character_class)
                self.assertGreater(len(requirements), 0)
