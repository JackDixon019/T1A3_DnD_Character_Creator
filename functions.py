from character import Character
from libraries import race_list, background_list, class_list, subclass_dictionary, stat_options
from dice_roller import roll_die

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
    hp_choice = check_input_within_given_range(input(f"How would you like to set a max HP?\n1. Roll\n2. Average"), 0, [1, 2])
    while hp_choice == "loop":
        hp_choice = check_input_within_given_range(input(f"How would you like to set a max HP?\n1. Roll\n2. Average"), 0, [1, 2])
    level_counter = starting_level + 1

    # These two steps are kinda combined into one awkwardly. 
    # max hp value is determined each time a character levels up, and every 4 levels a character gets the choice to increase their stats.
    # This may affect the hp gained
    while level_counter <= current_character.get_level():
        if level_counter % 4 == 0:
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
    return current_character.get_max_hp()


def create_character():
    # Name
    name = input("\nPlease enter your character's name: ")
    
    # Race
    race = select_race(name)

    # Background
    background = select_background(name)

    # Alignment
    alignment = input(f"\nPlease enter {name}'s alignment (E.G. Lawful Good): ")

    # Age
    age = input(f"\nPlease enter {name}'s age: ")

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
    print(f"\nHow would you like to determine {name}'s base stats?")
    for i in range(3):
        print(f"{i+1} {stat_options[i]}")

    stat_choice = check_input_within_given_range(input("\n"), 0, range(1,4))
    while stat_choice == "loop":
        stat_choice = check_input_within_given_range(input("\n"), 0, range(1,4))

    current_character.create_new_stats(stat_choice)

    increase_to_level(current_character, 0)

    # Create character
    return current_character

def get_dice():
    die_count = check_input_within_given_range(input("\nHow many die would you like to roll? (max 1000) "), 0, range(1, 1001)) 
    while die_count == "loop":
        die_count = check_input_within_given_range(input("\nHow many die would you like to roll? (max 1000) "), 0, range(1, 1001))
        
    die_type = check_input_within_given_range(input("\nHow many sides does the dice have? (max 1000) "), 0, range(1, 1001))
    while die_type == "loop":
        die_type = check_input_within_given_range(input("\nHow many sides does the dice have? (max 1000) "), 0, range(1, 1001))
    
    while True:
        # Advantage is only used in cases of rolling 2d20
        if die_count == 2 and die_type == 20:
            advantage = check_input_within_given_range(input("Do you have advantage?\n1. No\n2. I have advantage\n3. I have disadvantage :(\n"), 0, range(1,4))
            match advantage:
                case 1:
                    advantage = 0
                    break
                case 2:
                    advantage = 1
                    break
                case 3:
                    advantage = -1
                    break
                case _:
                    "Please enter either 1, 2, or 3"
        else:
            advantage = 0
            break

    return roll_die(die_count, die_type, advantage)



            
    