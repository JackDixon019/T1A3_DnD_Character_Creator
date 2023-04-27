from libraries import race_list, background_list, class_dictionary, subclass_dictionary, level_one_subclasses, level_two_subclasses

class LevelOutOfBounds(Exception):
    pass

class Character():
    def __init__(self, name, race, background, alignment, age, character_class, character_subclass, level, str, dex, con, int, wis, cha, max_hp):
        self._name = name
        self._race = race
        self._background = background
        self._alignment = alignment
        self._age = age
        self._character_class = character_class
        self._character_subclass = character_subclass
        self._level = level
        self._str = str
        self._dex = dex
        self._con = con
        self._int = int
        self._wis = wis
        self._cha = cha
        self._max_hp = max_hp

    def set_name(self):
        self._name = input("Please enter your character's name: ")

    def set_race(self):
        print(f"Please select {self._name}'s race from the following: ")
        for i in range(0, len(race_list)):
            print(f"{i+1}. {race_list[i]}")
        race_index = int(input())
        self._race = race_list[race_index-1]

    def set_background(self):
        print(f"Please select {self._name}'s background from the following:")
        for i in range(0, len(background_list)):
            print(f"{i+1}. {background_list[i]}")
        background_index = int(input()) - 1
        self._background = background_list[background_index]

    def set_alignment(self):
        self._alignment = input(f"Please enter {self._name}'s alignment (e.g. Lawful Good): ")

    def set_age(self):
        self._age = input(f"Please enter {self._name}'s age: ")

    def set_level(self):
        level = int(input(f"Please enter {self._name}'s level between 1 and 20: "))
        if 1 > level  or level > 20:
            raise LevelOutOfBounds("Please enter a level between 1 and 20")
        self._level = level

    def set_character_class(self):
        print(f"Please select {self._name}'s class from the following:")
        for i in range(0, len(class_dictionary)):
            print(f"{i+1}. {class_dictionary[i]}")
        class_index = int(input()) - 1
        self._character_class = class_dictionary[class_index]

    def set_character_subclass(self):
        has_subclass = self._level >= 3 or self._character_class in level_one_subclasses or (self._level >= 2 and self._character_class in level_two_subclasses)
        
        if has_subclass == True:
            print(f"Please select {self._name}'s subclass from the following:")
            for i in range(0, len(subclass_dictionary[self._character_class])):
                print(f"{i+1}. {subclass_dictionary[self._character_class][i]}")
            character_subclass = int(input()) - 1
            self._character_subclass = subclass_dictionary[self._character_class][character_subclass]
        else:
            print("Your character does not yet have a subclass unlocked.")

    def set_stats(self):
        pass

    def set_max_hp(self):
        pass

    def get_character(self):
        print(f"""
        Character name: {self._name},
        Race: {self._race},
        Background: {self._background},
        Alignment: {self._alignment},
        age: {self._age},
        character_class: {self._character_class},
        character_subclass: {self._character_subclass},
        level: {self._level},
        str: {self._str},
        dex: {self._dex},
        con: {self._con},
        int: {self._int},
        wis: {self._wis},
        cha: {self._cha},
        max_hp: {self._max_hp},
        """)


