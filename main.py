
from functions import create_character, get_dice
from files import save_character, edit_character, select_character, view_character, delete_character
import colored
from colored import fg, bg, attr, stylize

info = colored.fg("green")
options = colored.fg(218)
error = colored.fg("red")
variable = colored.fg("yellow")

# Main menu
try:
    while True:
        print(stylize("\nWelcome to The Tavern!\nWhat would you like to do here?", info))
        menu_select = input(stylize("""
        1. Create a character
        2. View a character
        3. Edit a character
        4. Delete a character
        5. Roll some dice
        6. Exit\n
        """, options))
        match menu_select:
            case "1":
                # Creates character object
                current_character = create_character()
                # Saves character
                save_character(current_character)
                print("\n")
                # Prints character values
                for key in current_character.get_character():
                    print(stylize(f"{key}: {current_character.get_character()[key]}", variable))
            case "2":
                # View character
                character_name = select_character("view")
                view_character(character_name)

            case "3":
                # Edit character
                character_name = select_character("edit")
                edit_character(character_name)
            case "4":
                # Delete character
                character_name = select_character("delete")
                delete_character(character_name)
            case "5":
                # Roll dice
                print(get_dice())
                
            case "6":
                # Quit
                print(stylize("\nProgram now exiting\n", error))
                break
            case _:
                print(stylize(f'\nInput not recognised\nPlease enter a number from the list provided', error))

# Whole program wrapped in try:except to catch stray errors.
except Exception as e:
    print(e)
    print(stylize("Something went wrong :(", error))
    

