from selectors import DefaultSelector
from libraries import race_list, background_list, class_list, subclass_dictionary, level_one_subclasses, level_two_subclasses, stat_options, default_stats

# Custom error for players entering too low or high of a level
class LevelOutOfBounds(Exception):
    pass
class TheBackrooms(Exception):
    pass

class Character():
    # Defines the characteristics of a character
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

    # Sets the character's name
    def set_name(self):
        self._name = input("\nPlease enter your character's name: ")

    # Sets the character's race from the race library
    def set_race(self):
        print(f"\nPlease select {self._name}'s race from the following: ")
        # Lists available options
        for i in range(0, len(race_list)):
            print(f"{i+1}. {race_list[i]}")
        race_index = int(input()) - 1
        self._race = race_list[race_index]

    # Sets the character's background from the backgrounds library
    def set_background(self):
        print(f"\nPlease select {self._name}'s background from the following:")
        # Lists available options
        for i in range(0, len(background_list)):
            print(f"{i+1}. {background_list[i]}")
        background_index = int(input("\n")) - 1
        self._background = background_list[background_index]

    # Sets the character's alignment (player-defined, but could be a dictionary of alignments)
    def set_alignment(self):
        self._alignment = input(f"\nPlease enter {self._name}'s alignment (e.g. Lawful Good): ")

    # Sets the character's age
    def set_age(self):
        self._age = input(f"\nPlease enter {self._name}'s age: ")

    # Sets the character's level. Errors if the level is outside of range
    def set_level(self):
        level = int(input(f"\nPlease enter {self._name}'s level between 1 and 20: "))
        if 1 > level  or level > 20:
            raise LevelOutOfBounds("Please enter a level between 1 and 20")
        self._level = level

    # Sets the character's class from the class list
    def set_character_class(self):
        print(f"\nPlease select {self._name}'s class from the following:")
        for i in range(0, len(class_list)):
            print(f"{i+1}. {class_list[i]}")
        class_index = int(input("\n")) - 1
        self._character_class = class_list[class_index]

    # Sets the character's subclass from the subclass dictionary
    # subclass_dicitonary has class as the key and a list of subclasses as the paired value
    def set_character_subclass(self):
        # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
        has_subclass = self._level >= 3 or self._character_class in level_one_subclasses or (self._level >= 2 and self._character_class in level_two_subclasses)
        
        if has_subclass == True:
            print(f"\nPlease select {self._name}'s subclass from the following:")
            # For the length of the list paired to the character's class:
            for i in range(0, len(subclass_dictionary[self._character_class])):
                # Prints each item in the list. I.E. prints each subclass.
                print(f"{i+1}. {subclass_dictionary[self._character_class][i]}")
            subclass_index = int(input("\n")) - 1
            self._character_subclass = subclass_dictionary[self._character_class][subclass_index]

        # If the character has not yet unlocked a subclass:
        else:
            print("\nYour character does not yet have a subclass unlocked.")

    # Setting stats done in 3 ways: point buy, roll 4d6 choose highest 3, and roll 3d6
    # For context, d6 is a 6-sided die. Highest score total is 20 (outside of magic).
    def set_stats(self):
        print(f"How would you like to determine {self._name}'s base stats?")
        for i in range(len(stat_options)):
            print(f"{i+1} {stat_options[i]}")
        method = int(input())
        match method:
            case 1:
                # In point-buy, the player's stats start at 8. The player then has 27 points total to spend across all 6 stats.
                # No one stat can exceed 15 points in this way
                total = 0
                retry = "y"
                # Allows player to reallocate if needed
                while retry == "y":
                    # Checks total points allocated meets the limit
                    if total < 27:
                        print(f"\nYou have {27-total} points remaining to allocate between each stat")
                        print("Each stat can have a maximum of 15 before bonuses are applied.")
                        print(f"Currently, {self._name}'s stats are:")
                        # lists each stat and value in the default_stats dicionary
                        for stat in default_stats:
                            print(f"{stat}: {default_stats[stat]}")
                        stat_choice = input("\nWhich stat would you like to allocate points to?\n").upper()
                        # Checks the stat chosen is less than 15
                        if default_stats[stat_choice] < 15:
                            # Gets the number of points the user wants to add
                            point_allocation = int(input(f"{stat_choice} has {min(15 - default_stats[stat_choice], 27-total)} available points remaining.\nHow many would you like to add?\n"))
                            # Checks the user's desired addition is legal (<15 total)
                            if point_allocation <= 15 - default_stats[stat_choice]:
                                # Adds additional points to stat and to total points tally
                                default_stats[stat_choice] += point_allocation
                                total += point_allocation
                            else:
                                print("Sorry, that's too many points for one stat. The maximum is 15\n")
                        else:
                            print("Sorry, that stat is already at the maximum. Please select another.")

                    # If the total points are >27:
                    elif total > 27:
                        print(f"\nSorry, {total} is too many points total.")
                        # Subtracts last points allocation from the most recent score + total points tally
                        default_stats[stat_choice] -= point_allocation
                        total -= point_allocation

                    # Prints character's current stats, and then offers the choice to reallocate them.
                    elif total == 27:
                        print(f"\n {self._name}'s stats are currently:")
                        for stat in default_stats:
                            print(f"{stat}: {default_stats[stat]}")
                        retry = input("\nWould you like to reallocate these stats? y/n \n").lower()
                        # If the user chooses not to reallocate, saves the values to the Character object
                        if retry != "y":
                            self._str = default_stats["STR"]
                            self._dex = default_stats["DEX"]
                            self._con = default_stats["CON"]
                            self._int = default_stats["INT"]
                            self._wis = default_stats["WIS"]
                            self._cha = default_stats["CHA"]
                            return
                        # If the user chooses to rellocate, resets default values to 8 and total to 0
                        else: 
                            for i in default_stats:
                                default_stats[i] = 8
                            total = 0
                    # Catches errors in case I did my math wrong somewhere lol
                    else:
                        raise TheBackrooms("How did you even get here?")
            case 2:
                pass
            case 3:
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


