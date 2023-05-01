from character import Character
from libraries import race_list, background_list, class_list, subclass_dictionary, stat_options

def check_input_within_given_range(prompt, index_correction, output_range):
    # This function prompts the user to try again if they input a value outside of the given range
    while True:
        try:
            output = int(input(prompt))
            output = output + index_correction
            if output not in output_range:
                raise ValueError
            else:
                return output
        except ValueError:
                print("Please enter a number from the available list only")

def select_race(name):
    print(f"\nPlease select {name}'s race from the following: ")
    # Lists available options
    for i in range(len(race_list)):
        print(f"{i+1}. {race_list[i]}")
    race_index = check_input_within_given_range("\n", -1, range(len(race_list)))
    return race_list[race_index]

def select_background(name):
    print(f"\nPlease select {name}'s background from the following:")
    # Lists available options
    for i in range(len(background_list)):
        print(f"{i+1}. {background_list[i]}")
    background_index = check_input_within_given_range("\n", -1, range(len(background_list)))
    return background_list[background_index]

def select_class(name):
    print(f"\nPlease select {name}'s class from the following:")
    for i in range(len(class_list)):
        print(f"{i+1}. {class_list[i]}")
    class_index = check_input_within_given_range("\n", -1, range(len(class_list)))
    return class_list[class_index]

def select_subclass(name, level, character_class):
    # If the character has not yet unlocked a subclass:
    if level < subclass_dictionary[character_class][0]:
        print("\nYour character does not yet have a subclass unlocked.")
        return "Subclass not yet unlocked"
    
    print(f"\nPlease select {name}'s subclass from the following:")
    # For the length of the list paired to the character's class:
    for i in range(2, len(subclass_dictionary[character_class])):
        # Prints each item in the list. I.E. prints each subclass.
        print(f"{i-1}. {subclass_dictionary[character_class][i]}")
    subclass_index = check_input_within_given_range("\n", 1, range(2, len(subclass_dictionary[character_class])))
    return subclass_dictionary[character_class][subclass_index]

def increase_to_level(current_character):
    hp_choice = check_input_within_given_range(f"How would you like to set a max HP?\n1. Roll\n2. Average", 0, [1, 2])
    level_counter = 1
    while level_counter <= current_character.get_level():
        if level_counter % 4 == 0:
            asi = check_input_within_given_range("\nWould you like: \n1. A Feat\n2. An Ability Score Increase?", 0, [1,2])
            if asi == 2:
                current_character.asi()
            else:
                print(f"Please refer to the Player's Handbook for a list of choosable Feats")
        current_character.set_max_hp(hp_choice)
        level_counter += 1
    return


def create_character():
    # Creates character with default statline and no details
    current_character = Character("dave", "", "None chosen", "None chosen", "None chosen", "None chosen", "No subclass chosen (yet)", 1, 8, 8, 8, 8, 8, 8, 0)

    # # Name
    name = input("\nPlease enter your character's name: ")
    current_character.set_name(name)
    
    # Race
    race = select_race(name)
    current_character.set_race(race)

    # # Background
    background = select_background(name)
    current_character.set_background(background)

    # Alignment
    alignment = input(f"Please enter {name}'s alignment (E.G. Lawful Good): ")
    current_character.set_alignment(alignment)

    # Age
    age = input(f"Please enter {name}'s age: ")
    current_character.set_age(age)

    # Level
    level = check_input_within_given_range(f"\nPlease enter {name}'s level between 1 and 20: ", 0, range(1, 21))

    current_character.set_level(level)
    
    # Class
    character_class = select_class(name)
    current_character.set_character_class(character_class)


    # Subclass
    # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
    subclass = select_subclass(name, level, character_class)
    current_character.set_character_subclass(subclass)

    # Stats
    print(f"How would you like to determine {name}'s base stats?")
    for i in range(len(stat_options)):
        print(f"{i+1} {stat_options[i]}")

    stat_choice = check_input_within_given_range("\n", 0, range(1,3))

    current_character.create_new_stats(stat_choice)

    increase_to_level(current_character)

    # Create character
    return current_character





        
