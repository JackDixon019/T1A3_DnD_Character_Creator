from functions import check_input_within_given_range, select_background, select_class, select_race, select_subclass, increase_to_level
import csv
from character import Character
import pprint
from os import listdir, remove

pp = pprint.PrettyPrinter(sort_dicts=False)

def view_character(character_name):
    filepath = f'./characters/{character_name}'
    try:
        with open(filepath, "r") as character_file:
            reader = csv.reader(character_file)
            reader.__next__()
            for row in reader:
                print(row)

    except FileNotFoundError as e:
        print("\nNo character with that name exists. Please check spelling and try again.")
        return "loop"
    
def select_character(verb):
    characters_list = listdir('./characters/')
    print(f"\nAvailable characters to {verb} are:\n")
    for i in range(len(characters_list)):
        print(f"{i+1}. {characters_list[i]}")
    character_index = check_input_within_given_range(input("\n"), -1, range(len(characters_list)))
    while character_index == "loop":
        character_index = check_input_within_given_range(input("\n"), -1, range(len(characters_list)))
    return characters_list[character_index]


def save_character(current_character):
    character_list = []
    character_data = current_character.get_character()
    for key in character_data:
        character_list.append([key, character_data[key]])
    name = current_character.get_name()
    while True:
        try:
            filepath = f'./characters/{name}'
            with open(filepath, "r") as character_file:
                pass
            print("\nA character with this name already exists. Do you want to overwrite?\n")
            overwrite = check_input_within_given_range(input("1. Yes\n2. No\n"), 0, range(1,3))
            while overwrite == "loop":
                overwrite = check_input_within_given_range(input("1. Yes\n2. No\n"), 0, range(1,3))
            if overwrite == 1:
                raise FileNotFoundError
            elif overwrite == 2:
                name = input("\nPlease enter an alternative name to save this character sheet as")

        except FileNotFoundError as e:
            with open(filepath, "w") as character_file:
                writer = csv.writer(character_file)
                writer.writerow(["Attribute","Value"])
                writer.writerows(character_list)
            print("Character saved!")
            return
    

def edit_character(character_name):
    value_list = []
    filepath = f'./characters/{character_name}'
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            value_list.append(row[1])
    current_character = Character(value_list[0], value_list[1], value_list[2],
                                  value_list[3], value_list[4], value_list[5], 
                                  value_list[6], int(value_list[7]), int(value_list[8]), 
                                  int(value_list[9]), int(value_list[10]), int(value_list[11]), 
                                  int(value_list[12]), int(value_list[13]), int(value_list[14]))
    while True:
        print("\nPlease select an attribute to edit from the list below, or type 'quit' to quit:\n")
        attribute_list = list(current_character.get_character().keys())
        name = current_character.get_name()

        for i in range(8):
            print(f"{i+1}. {attribute_list[i]}")
        attribute_index = input()
        match attribute_index:
            case "1":
                new_name = input("Please enter a new name:\n")
                current_character.set_name(new_name)
            case "2":
                race = select_race(name)
                current_character.set_race(race)
            case "3":
                background = select_background(name)
                current_character.set_background(background)
            case "4":
                alignment = input("Please enter a new alignment:\n")
                current_character.set_alignment(alignment)
            case "5":
                age = input(f"Please enter {name}'s age: ")
                current_character.set_age(age)
            case "6":
                character_class = select_class(name)
                current_character.set_character_class(character_class)
            case "7":
                character_class = current_character.get_character_class()
                level = int(current_character.get_level())
                print(type(level))
                # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
                subclass = select_subclass(name, level, character_class)
                current_character.set_character_subclass(subclass)     
            case "8":
                level = int(current_character.get_level())
                new_level = check_input_within_given_range(input(f"\nPlease enter {name}'s level between {level} and 20: "), 0, range(level, 21))
                # If input is outside of range or a ValueError, tries again
                while new_level == "loop":
                    new_level = check_input_within_given_range(input(f"\nPlease enter {name}'s level between {level} and 20: "), 0, range(level, 21))
                current_character.set_level(new_level)
                increase_to_level(current_character, new_level)
            case "quit":
                break
            case _:
                print("Please enter a number from the list provided")
                continue
        pp.pprint(current_character.get_character())
        save_character(current_character)

def delete_character(character_name):
    filepath = f'./characters/{character_name}'
    remove(filepath)
