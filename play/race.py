import sys

import definition


if sys.argv[1:] == ['--per-race']:
    for race in definition.Race._member_map_.values():
        print(f'{race.name.capitalize()}:')
        options = []
        for character_class in definition.Class._member_map_.values():
            requirements = definition.get_class_requirements(character_class)
            missing = 0
            for parameter, value in definition.get_race_parameters(race).items():
                if parameter in requirements and requirements[parameter] > value:
                    missing += requirements[parameter] - value
            options.append((character_class.name.capitalize().rjust(9), missing))
        for name, missing in sorted(options, key=lambda x: x[1]):
            print(f'  {name} — {missing}')

else:
    for character_class in definition.Class._member_map_.values():
        print(f'{character_class.name.capitalize()}:')
        requirements = definition.get_class_requirements(character_class)
        options = []
        for race in definition.Race._member_map_.values():
            missing = 0
            for parameter, value in definition.get_race_parameters(race).items():
                if parameter in requirements and requirements[parameter] > value:
                    missing += requirements[parameter] - value
            options.append((race.name.capitalize().rjust(9), missing))
        for name, missing in sorted(options, key=lambda x: x[1]):
            print(f'  {name} — {missing}')
