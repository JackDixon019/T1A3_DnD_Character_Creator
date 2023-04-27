
from character import Character, LevelOutOfBounds, TheBackrooms
from functions import create_character

print("Welcome to The Tavern! \n What would you like to do here?")


try:
    menu_select = int(input("""
    1. Create a character
    2. View a character
    3. Edit a character
    4. Delete a character
    5. Roll some dice
    6. Exit
    """))
    match menu_select:
        case 1:
            current_character = create_character()
            current_character.get_character()
        case 2:
            print("View Character")
        case 3:
            print("Edit Character")
        case 4:
            print("Delete Character")
        case 5:
            print("Roll Dice")
        case 6:
            print("Program now exiting")
            quit

except ValueError:
    print("Error, please enter a number from the list")

except LevelOutOfBounds as e:
    print("Please enter a level between 1 and 20")

except TheBackrooms as e:
    print("How did you even get here?")

except Exception as e:
    print(e)
    print("Something went wrong :(")
    

