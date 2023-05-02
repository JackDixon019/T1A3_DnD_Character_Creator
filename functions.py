from turtle import back
from character import Character
from libraries import race_list, background_list, class_list, subclass_dictionary, stat_options

def check_input_within_given_range(user_input, index_correction, expected_range):
    # This function prompts the user to try again if they input a value outside of the given range
    try:
        output = int(user_input) + index_correction
        if output not in expected_range:
            raise ValueError
        else:
            return output
    except ValueError:
            print("Please enter a number from the available list only")
            return "loop"

def select_race(name):
    print(f"\nPlease select {name}'s race from the following: ")
    # Lists available options
    for i in range(len(race_list)):
        print(f"{i+1}. {race_list[i]}")
    # Checks user input is within the available races list
    race_index = check_input_within_given_range(input("\n"), -1, range(len(race_list)))
    # If input is outside of range or a ValueError, tries again
    while race_index == "loop":
        race_index = check_input_within_given_range(input("\n"), -1, range(len(race_list)))
    return race_list[race_index]

def select_background(name):
    print(f"\nPlease select {name}'s background from the following:")
    # Lists available options
    for i in range(len(background_list)):
        print(f"{i+1}. {background_list[i]}")
    # Checks user input is within the available list
    background_index = check_input_within_given_range(input("\n"), -1, range(len(background_list)))
    # If input is outside of range or a ValueError, tries again
    while background_index == "loop":
        background_index = check_input_within_given_range(input("\n"), -1, range(len(background_list)))
    return background_list[background_index]

def select_class(name):
    print(f"\nPlease select {name}'s class from the following:")
    for i in range(len(class_list)):
        print(f"{i+1}. {class_list[i]}")
    # Checks user input is within the available list
    class_index = check_input_within_given_range(input("\n"), -1, range(len(class_list)))
    # If input is outside of range or a ValueError, tries again
    while class_index == "loop":
        class_index = check_input_within_given_range(input("\n"), -1, range(len(class_list)))
    return class_list[class_index]

def select_subclass(name, level, character_class):
    # subclass_dictionary[character_class][0] is the level a class' subclass is unlocked
    if level < subclass_dictionary[character_class][0]:
        print("\nYour character does not yet have a subclass unlocked.")
        return "Subclass not yet unlocked"
    
    print(f"\nPlease select {name}'s subclass from the following:")
    # For the length of the list paired to the character's class. 
    # Starts at position 2 because 0 and 1 are not subclasses
    for i in range(2, len(subclass_dictionary[character_class])):
        # Prints each item in the list. I.E. prints each subclass.
        print(f"{i-1}. {subclass_dictionary[character_class][i]}")
    # Checks user input is within the available list
    subclass_index = check_input_within_given_range(input("\n"), 1, range(2, len(subclass_dictionary[character_class])))
    # If input is outside of range or a ValueError, tries again
    while subclass_index == "loop":
        subclass_index = check_input_within_given_range(input("\n"), 1, range(2, len(subclass_dictionary[character_class])))
    return subclass_dictionary[character_class][subclass_index]

def increase_to_level(current_character, starting_level):
    # Checks user input is within the available list
    hp_choice = check_input_within_given_range(f"How would you like to set a max HP?\n1. Roll\n2. Average", 0, [1, 2])
    level_counter = starting_level

    # These two steps are kinda combined into one awkwardly. 
    # max hp value is determined each time a character levels up, and every 4 levels a character gets the choice to increase their stats.
    # This may affect the hp gained
    while level_counter < current_character.get_level():
        if level_counter % 4 == 0 and level_counter != 0:
            asi = check_input_within_given_range(input("\nWould you like: \n1. A Feat\n2. An Ability Score Increase?"), 0, [1,2])
            # If input is outside of range or a ValueError, tries again
            while asi == "loop":
                asi = check_input_within_given_range(input("\nWould you like: \n1. A Feat\n2. An Ability Score Increase?"), 0, [1,2])
            if asi == 2:
                current_character.assign_stats(current_character.get_stats(), 2, 20)
            else:
                print(f"Please refer to the Player's Handbook for a list of choosable Feats")
        current_character.set_max_hp(hp_choice)
        level_counter += 1
    return


def create_character():
    # Name
    name = input("\nPlease enter your character's name: ")
    
    # Race
    race = select_race(name)
    # current_character.set_race(race)

    # Background
    background = select_background(name)

    # Alignment
    alignment = input(f"Please enter {name}'s alignment (E.G. Lawful Good): ")

    # Age
    age = input(f"Please enter {name}'s age: ")

    # Level
    level = check_input_within_given_range(input(f"\nPlease enter {name}'s level between 1 and 20: "), 0, range(1, 21))
    # If input is outside of range or a ValueError, tries again
    while level == "loop":
        level = check_input_within_given_range(input(f"\nPlease enter {name}'s level between 1 and 20: "), 0, range(1, 21))
    
    # Class
    character_class = select_class(name)


    # Subclass
    # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
    subclass = select_subclass(name, level, character_class)

    # Creates character with information provided + default stat-line
    current_character = Character(name, race, background, alignment, age, character_class, subclass, level, 8, 8, 8, 8, 8, 8, 0)

    # Stats
    print(f"How would you like to determine {name}'s base stats?")
    for i in range(6):
        print(f"{i+1} {stat_options[i]}")

    stat_choice = check_input_within_given_range(input("\n"), 0, range(1,3))
    while stat_choice == "loop":
        stat_choice = check_input_within_given_range(input("\n"), 0, range(1,3))

    current_character.create_new_stats(stat_choice)

    increase_to_level(current_character, 0)

    # Create character
    return current_character





        
