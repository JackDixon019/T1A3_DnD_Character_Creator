
from functions import create_character, get_dice
from files import save_character, edit_character, select_character, view_character, delete_character

# Main menu
try:
    while True:
        print("\nWelcome to The Tavern! \nWhat would you like to do here?")
        menu_select = input("""
        1. Create a character
        2. View a character
        3. Edit a character
        4. Delete a character
        5. Roll some dice
        6. Exit\n
        """)
        match menu_select:
            case "1":
                # Creates character object
                current_character = create_character()
                # Saves character
                save_character(current_character)
                print("\n")
                # Prints character values
                for key in current_character.get_character():
                    print(f"{key}: {current_character.get_character()[key]}")
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
                print("Program now exiting")
                break
            case _:
                print("Please enter a number from the list")

# Whole program wrapped in try:except to catch stray errors.
except Exception as e:
    print(e)
    print("Something went wrong :(")
    

