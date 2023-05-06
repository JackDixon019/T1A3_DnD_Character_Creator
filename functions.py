from character import Character
from libraries import race_list, background_list, class_list, subclass_dictionary, stat_options
from dice_roller import roll_die
import colored
from colored import stylize

info = colored.fg("green")
options = colored.fg(218)
error = colored.fg("red")

def check_input_within_given_range(user_input, index_correction, expected_range):
    # This function prompts the user to try again if they input a value outside of the given range
    try:
        output = int(user_input) + index_correction
        if output not in expected_range:
            raise ValueError
        else:
            return output
    except ValueError:
            print(stylize("\nPlease enter a number from the available list only", error))
            return "loop"

def print_list(name, attribute, list_name,  offset = 1, range_start = 0):
    print(stylize(f"\nPlease select {name}'s {attribute} from the following: ", info))
    for i in range(range_start, len(list_name)):
        print(stylize(f"{i+offset}. {list_name[i]}", options))

def input_loop(list_name, prompt = "\n", range_start = 0, index_correction = -1):
    index = check_input_within_given_range(input(prompt), index_correction, range(range_start, len(list_name)))
    while index == "loop":
        index = check_input_within_given_range(input(prompt), index_correction, range(range_start, len(list_name)))
    return list_name[index]

def select_race(name):
    # Lists available options, receives user input, checks user input, returns corresponding value
    print_list(name, "race", race_list)
    return input_loop(race_list)


def select_background(name):
    # Lists available options, receives user input, checks user input, returns corresponding value
    print_list(name, "background", background_list)
    return input_loop(background_list)

def select_class(name):
    # Lists available options
    print_list(name, "class", class_list)
    return input_loop(class_list)


def select_subclass(name, level, character_class):
    # subclass_dictionary[character_class][0] is the level a class' subclass is unlocked
    if level < subclass_dictionary[character_class][0]:
        print(stylize("\nYour character does not yet have a subclass unlocked.", colored.fg("yellow")))
        return "Subclass not yet unlocked"

    # Lists available options, receives user input, checks user input, returns corresponding value
    # Starts at position 2 because 0 and 1 are not subclasses
    print_list(name, "subclass", subclass_dictionary[character_class], -1, 2)
    return input_loop(subclass_dictionary[character_class], "\n", 2, 1)

def increase_to_level(current_character, starting_level):
    # Checks user input is within the available list
    hp_choice = input_loop([1,2], stylize(f"\nHow would you like to set a max HP?", info) + stylize("\n1. Roll\n2. Average\n", options))
    level_counter = starting_level + 1

    # These two steps are kinda combined into one awkwardly. 
    # max hp value is determined each time a character levels up, and every 4 levels a character gets the choice to increase their stats.
    # This may affect the hp gained
    while level_counter <= current_character.get_level():
        if level_counter % 4 == 0:
            asi = input_loop([1,2], stylize("\nWould you like:", info) + stylize(" \n1. A Feat\n2. An Ability Score Increase?", options))
            if asi == 2:
                current_character.assign_stats(current_character.get_stats(), 2, 20)
            else:
                print(f"Please refer to the Player's Handbook for a list of choosable Feats")
        current_character.set_max_hp(hp_choice)
        level_counter += 1
    return current_character.get_max_hp()


def create_character():
    # Name
    name = input(stylize("\nPlease enter your character's name: ", info))
    
    # Race
    race = select_race(name)

    # Background
    background = select_background(name)

    # Alignment
    alignment = input(stylize(f"\nPlease enter {name}'s alignment (E.G. Lawful Good): ", info))

    # Age
    age = input(stylize(f"\nPlease enter {name}'s age: ", info))

    # Level
    level = input_loop(range(1,21), stylize(f"\nPlease enter {name}'s level between 1 and 20: ", info))
    
    # Class
    character_class = select_class(name)


    # Subclass
    # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
    subclass = select_subclass(name, level, character_class)

    # Creates character with information provided + default stat-line
    current_character = Character(name, race, background, alignment, age, character_class, subclass, level, 8, 8, 8, 8, 8, 8, 0)

    # Stats
    print(stylize(f"\nHow would you like to determine {name}'s base stats?", info))
    for i in range(3):
        print(stylize(f"{i+1} {stat_options[i]}", options))

    stat_choice = input_loop(range(1,4))

    current_character.create_new_stats(stat_choice)

    increase_to_level(current_character, 0)

    # Create character
    return current_character

def get_dice():
    die_count = input_loop(range(1, 1001), stylize("\nHow many die would you like to roll? (max 1000) ", info))
        
    die_type = input_loop(range(2, 1001), stylize("\nHow many sides does the dice have? (min 2, max 1000) ", info), 0, -2)
    
    while True:
        # Advantage is only used in cases of rolling 2d20
        if die_count == 2 and die_type == 20:
            advantage = check_input_within_given_range(input(stylize("Do you have advantage?", info)+ stylize("\n1. No\n2. I have advantage\n3. I have disadvantage :(\n", options)), 0, range(1,4))
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
                    print(stylize("Please enter either 1, 2, or 3", error))
        else:
            advantage = 0
            break

    return roll_die(die_count, die_type, advantage)



            
    