
from character import Character, LevelOutOfBounds, TheBackrooms
from functions import create_character
from dice_roller import roll_die




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
                current_character.get_character()
            case "2":
                print("View Character")
            case "3":
                print("Edit Character")
            case "4":
                print("Delete Character")
            case "5":
                print("Roll Dice")
                while True:
                    try:
                        die_count = int(input("How many die would you like to roll? "))
                        break
                    except ValueError:
                        print("Error, please enter a number\n")
                        continue
                while True:
                    try:
                        die_type = int(input("How many sides does the dice have? "))
                        break
                    except ValueError:
                        print("Error, please enter a number\n")
                        continue

                
                while True:
                    try:
                        # Advantage is only used in cases of rolling 2d20
                        if die_count == 2 and die_type == 20:
                            advantage = int(input("Do you have advantage?\n1. No\n2. I have advantage\n3. I have disadvantage :(\n"))
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
                    except ValueError:
                        print("Error, please enter a number\n")
                        continue
                print(roll_die(die_count, die_type, advantage)) 
            case "6":
                print("Program now exiting")
                break
            case _:
                print("Input not recognised. Please enter a number from the list")
                pass

except ValueError:
    print("Error, please enter a number\n")

except LevelOutOfBounds as e:
    print("Please enter a level between 1 and 20")

except TheBackrooms as e:
    print("How did you even get here?")

except Exception as e:
    print(e)
    print("Something went wrong :(")
    

