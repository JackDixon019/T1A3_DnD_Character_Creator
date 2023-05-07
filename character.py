
from math import floor
from libraries import default_stats, subclass_dictionary
from dice_roller import roll_die, assign_score_to_stat
import colored
from colored import stylize

info = colored.fg("green")
options = colored.fg(218)
error = colored.fg("red")
variable = colored.fg("yellow")

class Character():
    # Defines the characteristics of a character
    def __init__(self, name, race, background, 
                 alignment, age, character_class, 
                 character_subclass, level, str, 
                 dex, con, int, wis, cha, max_hp):
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
        print(stylize(f"\n{self._name}'s stats are:", variable))
        for stat in new_stats:
            print(stylize(f"{stat}: {new_stats[stat]}", variable))
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
        # Creates new stats dictionary
        new_stats = {}
        # Copies values from stats parameter
        for stat in stats:
            new_stats[stat] = stats[stat]
        total = 0
        # While True loop keeps the stats from being reset
        while True:
            # Checks total points allocated meets the limit
            if total < points_to_assign:
                print(stylize(f"\nYou have", info) + stylize(f" {points_to_assign-total}", variable) + 
                      stylize(" points remaining to allocate between each stat.\nEach stat can have a maximum of ", info) + 
                      stylize(f"{max_stat}", variable) + stylize(f" before bonuses are applied.\nCurrently, {self._name}'s stats are:", info))
                # lists each stat and value in the default_stats dicionary
                for stat in new_stats:
                    print(stylize(f"{stat}: {new_stats[stat]}", options))
                print(stylize("\nWhich stat would you like to allocate points to?\n", info))
                stat_choice = input("\n").upper()

                # Checks for if the stat chosen is in the list of stats and the stat chosen is less than max_stat
                if stat_choice in list(new_stats) and new_stats[stat_choice] < max_stat:
                    try:
                        # Gets the number of points the user wants to add
                        point_allocation = int(input(stylize(f"\n{stat_choice} has ", info) + 
                                                     stylize(f"{min(max_stat - new_stats[stat_choice], points_to_assign-total)}", variable) + 
                                                     stylize(f" available points remaining.\nHow many would you like to add?\n", info)))
                        # Checks the user's desired addition is legal (<max_stat total)
                        if point_allocation <= max_stat - new_stats[stat_choice]:
                            # Adds additional points to stat and to total points tally
                            new_stats[stat_choice] += point_allocation
                            total += point_allocation
                        else:
                            print(stylize(f"\n\nSorry, that's too many points for one stat. The maximum is {max_stat}\n", error))

                    # Will catch if user enters non-integer characters and re-loop
                    except ValueError:
                        print(stylize("Please enter a number only", error))

                # Catches if stat is in list, but the value > max-limit
                elif stat_choice in list(new_stats):
                    print(stylize("\n\nSorry, that stat is already at the maximum. Please select another.", error))
                
                # If chosen stat is not in the list, prompts the user to try again
                else:
                    print(stylize("\n\nPlease enter an available stat", error))


            # If the total points are >points_to_assign:
            elif total > points_to_assign:
                print(stylize(f"\nSorry, {total} is too many points total.", error))
                # Subtracts last points allocation from the most recent score + total points tally
                new_stats[stat_choice] -= point_allocation
                total -= point_allocation

            # Prints character's current stats, and then offers the choice to reallocate them.
            elif total == points_to_assign:
                print(stylize(f"\n {self._name}'s stats are currently:", info))
                for stat in new_stats:
                    print(stylize(f"{stat}: {new_stats[stat]}", info))
                while True:
                    retry = input(stylize("\nAre you happy with this stat distribution?", info) + 
                                  stylize("\n1. Yes, please save these stats.\n2. No, I'd like to try again.\n", options))
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
                        print(stylize("\n\nPlease select from either option 1 or option 2", error))

    # Setting stats done in 3 ways: point buy, roll 4d6 choose highest 3, and roll 3d6
    # For context, d6 is a 6-sided die. Highest score total is 20 (outside of magic).
    def create_new_stats(self, method):
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
            # This is the same as the prior method, only with 3x 6-dided die instead of 4, and no die removed.
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
        # modifier is the rounded-down value of (CON-10)/2
        modifier = floor((self._con - 10)/2)

        # Hill Dwarves have +1hp/level
        # I didn't actually make a Hill Dwarf race yet though... call it future-proofing
        if self._race == "Hill Dwarf":
            self._max_hp += 1
        
        # at level 1, max hp is calculated using the highest possible roll of a characters hit-die
        # Normally default max_hp == 0, but if the character is a Hill Dwarf then it would be 1... call it future-proofing
        if self._max_hp <= 1:
            self._max_hp += modifier + subclass_dictionary[self._character_class][1]
            return
        
        # If player selected to roll for max hp, rolls the character's hit-die and adds to the CON modifier
        elif roll == 1:
            self._max_hp += modifier + roll_die(1, subclass_dictionary[self._character_class][1],0)
        
        # Otherwise, takes the (rounded-up) average roll of the character's hit-die
        else:
            self._max_hp += modifier + subclass_dictionary[self._character_class][1]/2 + 1
        
        # If the player has the subclass Draconic Bloodline, increases hp by 1
        # This is applied AFTER the level-1 check, because Sorcerer subclass is chosen at level 2
        if self._character_subclass == "Draconic Bloodline":
            self._max_hp += 1
        
        # converts max_hp to an integer. Otherwise it would be a float thanks to the division earlier in the function
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



