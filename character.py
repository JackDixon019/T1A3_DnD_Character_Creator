
from math import floor
from libraries import default_stats, subclass_dictionary
from dice_roller import roll_die, assign_score_to_stat



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
    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    # Sets the character's race from the race library
    def set_race(self, race):
        self._race = race

    def get_race(self):
        return self._race

    # Sets the character's background from the backgrounds library
    def set_background(self, background):
        self._background = background

    def get_background(self):
        return self._background

    # Sets the character's alignment (player-defined, but could be a dictionary of alignments)
    def set_alignment(self, alignment):
        self._alignment = alignment
    
    def get_alignment(self):
        return self._alignment

    # Sets the character's age
    def set_age(self, age):
        self._age = age
    
    def get_age(self):
        return self._age

    # Sets the character's level. Errors if the level is outside of range
    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level



    # Sets the character's class from the class list
    def set_character_class(self, character_class):
        self._character_class = character_class

    def get_character_class(self):
        return self._character_class
        
    # Sets the character's subclass from the subclass dictionary
    # subclass_dicitonary has class as the key and a list of subclasses as the paired value
    def set_character_subclass(self, character_subclass):
        self._character_subclass = character_subclass

    def get_character_subclass(self):
        return self._character_subclass

    # Assigns values from a dictionary of ("stat" : score) pairs
    def set_stats(self, new_stats):
        print(f"\n{self._name}'s stats are:")
        for stat in new_stats:
            print(f"{stat}: {new_stats[stat]}")
        self._str = new_stats["STR"]
        self._dex = new_stats["DEX"]
        self._con = new_stats["CON"]
        self._int = new_stats["INT"]
        self._wis = new_stats["WIS"]
        self._cha = new_stats["CHA"]
        return
    
    def get_stats(self):
        stats = {}
        stats["STR"] = self._str
        stats["DEX"] = self._dex
        stats["CON"] = self._con
        stats["INT"] = self._int
        stats["WIS"] = self._wis
        stats["CHA"] = self._cha
        return stats
    
    def assign_stats(self, stats, points_to_assign, max_stat):
        new_stats = {}
        for stat in stats:
            new_stats[stat] = stats[stat]
        total = 0
        # While True loop keeps the stats from being reset
        while True:
            # Checks total points allocated meets the limit
            if total < points_to_assign:
                print(f"\nYou have {points_to_assign-total} points remaining to allocate between each stat.\nEach stat can have a maximum of {max_stat} before bonuses are applied.\nCurrently, {self._name}'s stats are:")
                # lists each stat and value in the default_stats dicionary
                for stat in new_stats:
                    print(f"{stat}: {new_stats[stat]}")
                stat_choice = input("\nWhich stat would you like to allocate points to?\n").upper()

                # Match case checks for if the stat chosen is in the list of stats and the stat chosen is less than max_stat
                if stat_choice in list(new_stats) and new_stats[stat_choice] < max_stat:
                    
                    try:
                        # Gets the number of points the user wants to add
                        point_allocation = int(input(f"{stat_choice} has {min(max_stat - new_stats[stat_choice], points_to_assign-total)} available points remaining.\nHow many would you like to add?\n"))
                        # Checks the user's desired addition is legal (<max_stat total)
                        if point_allocation <= max_stat - new_stats[stat_choice]:
                            # Adds additional points to stat and to total points tally
                            new_stats[stat_choice] += point_allocation
                            total += point_allocation
                        else:
                            print(f"\n\nSorry, that's too many points for one stat. The maximum is {max_stat}\n")

                    # Will catch if user enters non-integer characters and re-loop
                    except ValueError:
                        print("Please enter a number only")
                        
                elif stat_choice in list(new_stats):
                    print("\n\nSorry, that stat is already at the maximum. Please select another.")
                else:
                    # If chosen stat is not in the list, prompts the user to try again
                    print("\n\nPlease enter an available stat")


            # If the total points are >points_to_assign:
            elif total > points_to_assign:
                print(f"\nSorry, {total} is too many points total.")
                # Subtracts last points allocation from the most recent score + total points tally
                new_stats[stat_choice] -= point_allocation
                total -= point_allocation

            # Prints character's current stats, and then offers the choice to reallocate them.
            elif total == points_to_assign:
                print(f"\n {self._name}'s stats are currently:")
                for stat in new_stats:
                    print(f"{stat}: {new_stats[stat]}")
                while True:
                    retry = input("\nAre you happy with this stat distribution?\n1. Yes, please save these stats.\n2. No, I'd like to try again.\n")
                    # If the user chooses not to reallocate, saves the values to the Character object
                    if retry == "1":
                        self.set_stats(new_stats)
                        return
                    # If the user chooses to reallocate, resets default values to 8 and total to 0. 
                    elif retry == "2":
                        for stat in stats:
                            new_stats[stat] = stats[stat]
                        total = 0
                        break
                    # If the user enters an option not listed, prompts them to select a correct option
                    else: 
                        print("\n\nPlease select from either option 1 or option 2")



    # Setting stats done in 3 ways: point buy, roll 4d6 choose highest 3, and roll 3d6
    # For context, d6 is a 6-sided die. Highest score total is 20 (outside of magic).
    def create_new_stats(self, method):
        while True:
            # User has selected "point-buy"
            if method == 1:
                self.assign_stats(default_stats, 27, 15)
                return
            
            # User has selected roll "4d6 pick 3"
            elif method == 2:
                # In this case, we will simulate rolling 4 6-sided die and take the sum of the highest 3 rolls
                available_scores = []
                # For each stat
                for x in range(6):
                    # Rolls (4, 6-sided die, with "advantage") --> "advantage" removes lowest number from list of values
                    rolls = roll_die(4,6,1)
                    # Adds sum of rolls to available scores list
                    available_scores.append(rolls)
                # Sorts in descending order
                available_scores.sort(reverse=True)
                    
                # assigns scores to stats
                new_stats = assign_score_to_stat(available_scores)
                # assigns attributes to object
                self.set_stats(new_stats)
                return


            elif method == 3:
                # This is the same as the prior method, only with 3x 6-dided die instead of 4
                available_scores = []
                # For each stat
                for x in range(6):
                    # Rolls (3, 6-sided die, without "advantage")
                    available_scores.append(roll_die(3,6,0))

                # Sorts scores in descending order
                available_scores.sort(reverse=True)

                # Assigns scores to stats and stats to object
                new_stats = assign_score_to_stat(available_scores)
                self.set_stats(new_stats)
                return

    def set_max_hp(self, roll):
        modifier = floor((self._con - 10)/2)
        if self._race == "Hill Dwarf":
            self._max_hp += 1
        if self._max_hp <= 1:
            self._max_hp += modifier + subclass_dictionary[self._character_class][1]
            return
        elif roll == "1":
            self._max_hp += modifier + roll_die(1, subclass_dictionary[self._character_class][1],0)
        else:
            self._max_hp += modifier + subclass_dictionary[self._character_class][1]/2 + 1
        if self._character_subclass == "Draconic Bloodline":
            self._max_hp += 1
        self._max_hp = int(self._max_hp)
        return
    
    def get_max_hp(self):
        return self._max_hp

    def get_character(self):
        return {
        "Character Name" : self._name,
        "Race" : self._race,
        "Background" : self._background,
        "Alignment" : self._alignment,
        "Age" : self._age,
        "Class" : self._character_class,
        "Subclass" : self._character_subclass,
        "Level" : self._level,
        "STR" : self._str,
        "DEX" : self._dex,
        "CON" : self._con,
        "INT" : self._int,
        "WIS" : self._wis,
        "CHA" : self._cha,
        "Max HP" : self._max_hp
        }



