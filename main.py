
from character import Character, LevelOutOfBounds, TheBackrooms
from functions import create_character, get_dice




try:
    while True:
        print("Welcome to The Tavern! \n What would you like to do here?")
        menu_select = input("""
        1. Create a character
        2. View a character
        3. Edit a character
        4. Delete a character
        5. Roll some dice
        6. Exit
        """)
        match menu_select:
            case "1":
                current_character = create_character()
                print(current_character.get_character())
            case "2":
                print("View Character")
            case "3":
                print("Edit Character")
            case "4":
                print("Delete Character")
            case "5":
                print("Roll Dice")
                print(get_dice())
                
            case "6":
                print("Program now exiting")
                break
            case _:
                print("Please enter a number from the list")

except Exception as e:
    print(e)
    print("Something went wrong :(")
    

