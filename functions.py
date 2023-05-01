
from multiprocessing import Value
from character import Character
from random import randint
from libraries import race_list, background_list, class_list, subclass_dictionary, level_one_subclasses, level_two_subclasses, stat_options


def create_character():
    # Creates character with default statline and no details
    current_character = Character("dave", "", "None chosen", "None chosen", "None chosen", "None chosen", "No subclass chosen (yet)", 1, 8, 8, 8, 8, 8, 8, 0)

    # # Name
    name = input("\nPlease enter your character's name: ")
    current_character.set_name(name)
    
    # # Race
    while True:
            print(f"\nPlease select {name}'s race from the following: ")
            # Lists available options
            for i in range(len(race_list)):
                print(f"{i+1}. {race_list[i]}")
            try:
                race_index = int(input()) - 1
                if race_index not in range(len(race_list)):
                     raise ValueError
                else:
                    race = race_list[race_index]
                    break

            except ValueError:
                print("Please enter a number from the available list only")
        
    current_character.set_race(race)

    # # Background
    while True:
            print(f"\nPlease select {current_character._name}'s background from the following:")
            # Lists available options
            for i in range(len(background_list)):
                print(f"{i+1}. {background_list[i]}")
            try:
                background_index = int(input("\n")) - 1
                if background_index not in range(len(background_list)):
                    raise ValueError
                else:
                    background = background_list[background_index]
                    break

            except ValueError:
                print("Please enter a number from the available list only")
    current_character.set_background(background)

    # Alignment
    alignment = input(f"Please enter {name}'s alignment (E.G. Lawful Good): ")
    current_character.set_alignment(alignment)

    # Age
    age = input(f"Please enter {name}'s age: ")
    current_character.set_age(age)

    # Level
    while True:
        try:
            level = int(input(f"\nPlease enter {name}'s level between 1 and 20: "))
            if level not in range(1, 21):
                raise ValueError
            else:
                 break
        except ValueError:
            print("Please enter a number between 1 and 20")
    current_character.set_level(level)
    
    # Class
    while True:
        try:
            print(f"\nPlease select {name}'s class from the following:")
            for i in range(len(class_list)):
                print(f"{i+1}. {class_list[i]}")
            class_index = int(input("\n")) - 1
            if class_index not in range(len(class_list)):
                raise ValueError
            else:
                character_class = class_list[class_index]
                break
        except ValueError:
            print("Please enter a number from the available list only")

    current_character.set_character_class(character_class)

    # Subclass
    # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
    
    if level < subclass_dictionary[character_class][0]:
        print("\nYour character does not yet have a subclass unlocked.")
        character_subclass = "Subclass not yet unlocked"

    else:
        while True:
            try:
                print(f"\nPlease select {name}'s subclass from the following:")
                # For the length of the list paired to the character's class:
                for i in range(2, len(subclass_dictionary[character_class])):
                    # Prints each item in the list. I.E. prints each subclass.
                    print(f"{i-1}. {subclass_dictionary[character_class][i]}")
                subclass_index = int(input("\n")) + 1
                if 2 <= subclass_index < len(subclass_dictionary[character_class]):
                    character_subclass = subclass_dictionary[character_class][subclass_index]
                    break
                else:
                    raise ValueError

            except ValueError:
                print("Please enter a number from the list provided")

    # If the character has not yet unlocked a subclass:
    current_character.set_character_subclass(character_subclass)

    # Stats
    print(f"How would you like to determine {name}'s base stats?")
    for i in range(len(stat_options)):
        print(f"{i+1} {stat_options[i]}")
    method = input() 
    
    while method not in ["1", "2", "3"]: 
        method = input("Please enter a number from the list provided.")
    current_character.create_new_stats(method)

    current_character.set_max_hp()
                
    # Create character
    return current_character





        
