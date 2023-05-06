from asyncore import loop
import csv
import pprint
from os import listdir, remove

from functions import input_loop, select_background, select_class, select_race, select_subclass, increase_to_level
from character import Character
import colored
from colored import stylize

info = colored.fg("green")
options = colored.fg(218)
error = colored.fg("red")
variable = colored.fg("yellow")

# This prevents pprint from sorting the dictionaries alphabetically.
pp = pprint.PrettyPrinter(sort_dicts=False)


def select_character(verb):
    # Creates a list of files in the directory
    characters_list = listdir('./characters/')
    # {verb} contextually changes based on why the user is selecting a character (delete, view, edit etc.)
    print(stylize(f"\nAvailable characters to {verb} are:\n", info))
    # prints the name of each file in a numbered list
    for i in range(len(characters_list)):
        print(stylize(f"{i+1}. {characters_list[i]}", options))
    # receives user input. checks it is within the range of numbers provided
    character_index = input_loop(characters_list)
    return character_index

def view_character(character_name):
    filepath = f'./characters/{character_name}'
    print("\n")
    try:
        # If the file exists, prints each row (except the title row)
        with open(filepath, "r") as character_file:
            reader = csv.reader(character_file)
            reader.__next__()
            for row in reader:
                print(stylize(row, variable))
    # Catches if file does not exist.
    except FileNotFoundError as e:
        print(stylize("\nNo character with that name exists. Please check spelling and try again.", error))
        return "loop"
    

def save_character(current_character):
    character_list = []
    # gets a dicitonary of character stats and values
    character_data = current_character.get_character()
    # each key and value pair is assigned a list within the list character_list
    for key in character_data:
        character_list.append([key, character_data[key]])
    name = current_character.get_name()
    while True:
        try:
            filepath = f'./characters/{name}'
            # If the file can open, checks with the user if they want to overwrite
            with open(filepath, "r") as character_file:
                pass
            print(stylize("\nNow saving character", variable))
            print(stylize("\nA character with this name already exists. Do you want to overwrite?\n", info))
            overwrite = input_loop(range(1,3), stylize("1. Yes\n2. No\n", options))
            if overwrite == 1:
                raise FileNotFoundError
            elif overwrite == 2:
                name = input(stylize("\nPlease enter an alternative name to save this character sheet as:\n", info))
        # If no file is found, or if user chooses to overwrite, writes character_list to csv file
        except FileNotFoundError as e:
            with open(filepath, "w") as character_file:
                writer = csv.writer(character_file)
                writer.writerow(["Attribute","Value"])
                writer.writerows(character_list)
            print(stylize("\nCharacter saved!", variable))
            return
    

def edit_character(character_name):
    value_list = []
    filepath = f'./characters/{character_name}'
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        reader.__next__()
        # assigns each value from the character sheet to a list
        for row in reader:
            value_list.append(row[1])
    # each value from the list is called and assigned to the current_character object in the Character() class
    current_character = Character(value_list[0], value_list[1], value_list[2],
                                  value_list[3], value_list[4], value_list[5], 
                                  value_list[6], int(value_list[7]), int(value_list[8]), 
                                  int(value_list[9]), int(value_list[10]), int(value_list[11]), 
                                  int(value_list[12]), int(value_list[13]), int(value_list[14]))
    while True:
        print(stylize("\nPlease select an attribute to edit from the list below, or type 'quit' to save and quit:\n", info))
        attribute_list = list(current_character.get_character().keys())
        name = current_character.get_name()
        
        # prints each attribute (aside from stats) in a numbered list
        for i in range(8):
            print(stylize(f"{i+1}. {attribute_list[i]}", options))
        print(stylize("Or type 'quit' to quit\n", options))
        attribute_index = input().lower()
        match attribute_index:
            # for each input, allows the user to edit the corrersponding attribute
            # editing handled with same functions used to create character
            case "1":
                # change name
                new_name = input(stylize("Please enter a new name:\n", info))
                current_character.set_name(new_name)
            case "2":
                # change race
                race = select_race(name)
                current_character.set_race(race)
            case "3":
                # change bakground 
                background = select_background(name)
                current_character.set_background(background)
            case "4":
                # change alignment
                alignment = input(stylize("Please enter a new alignment:\n", info))
                current_character.set_alignment(alignment)
            case "5":
                # change age
                age = input(stylize(f"Please enter {name}'s age:\n", info))
                current_character.set_age(age)
            case "6":
                # change class
                character_class = select_class(name)
                current_character.set_character_class(character_class)
                # changing class necessitates changing subclass as well, so both are called here
                level = current_character.get_level()
                subclass = select_subclass(name, level, character_class)
                current_character.set_character_subclass(subclass) 
            case "7":
                # change subclass
                character_class = current_character.get_character_class()
                level = current_character.get_level()
                # Checks whether character has a subclass unlocked (unlocks at varying levels per class)
                subclass = select_subclass(name, level, character_class)
                current_character.set_character_subclass(subclass)     
            case "8":
                # change level
                starting_level = int(current_character.get_level())
                next_level = starting_level + 1
                new_level = input_loop(range(next_level, 21), stylize(f"\nPlease enter {name}'s level between {next_level} and 20: ", info), 0, -next_level)
                current_character.set_level(new_level)
                increase_to_level(current_character, starting_level)
            case "quit":
                break
            case _:
                # if unexpected value is entered, prompts the user to try again
                print(stylize("Please enter a number from the list provided", error))
                continue
        # pretty-prints character data
        pp.pprint(current_character.get_character())
        # saves character
        save_character(current_character)

def delete_character(character_name):
    filepath = f'./characters/{character_name}'
    try:
        remove(filepath)
    except FileNotFoundError as e:
        print("File already removed.")
    
