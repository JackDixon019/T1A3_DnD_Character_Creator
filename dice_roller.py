from random import randint
from libraries import default_stats


# Takes number of dice to roll, the sides of the dice, and if the user has advantage
def roll_die(number_of_die, dice_to_roll, advantage):
    rolls = []
    for i in range(number_of_die):
        # "rolls" a pseudorandom integer between 1 and the number of sides on the die --> simulating a d6
        roll = randint(1,dice_to_roll)
        # Stores roled value in list
        rolls.append(roll)
    print(rolls)
    if advantage == 1:
        # When player has advantage, removes lowest value rolled
        rolls.pop(rolls.index(min(rolls)))
    elif advantage == -1:
        # When player has disadvantage, removes highest value rolled
        rolls.pop(rolls.index(max(rolls)))

    return sum(rolls)


# This is just here to prevent import loop errors
# called after rolling dice in the assigning base stats phase of character creation
def assign_score_to_stat(available_scores):
    # creates a dictionary that will be filled with stat:score key:value pairs
    new_stats = {}
    # makes a list of stats available
    available_stats = list(default_stats.keys())
    print("\nYour available rolls are:\n")
    for i in available_scores:
        print(i)
    # While there are values in the list of stats available to edit:
    while available_stats != []:
        for score in available_scores:
            print(f"\nThe next score to assign is: {score}\n")
            print(f"The available stats to assign a score to are:")
            for stat in available_stats:
                print(stat)
            while True:
                # allows the user to input a value.
                chosen_stat = input(f"Please enter a stat you would like to assign the score {score}:\n").upper()
                match chosen_stat:
                    # For each stat, if user input.upper() matches a stat
                    case "STR":
                        # adds stat:score to the dictionary new_stats
                        new_stats["STR"] = score
                        # removes the stat from the list of available stats
                        available_stats.pop(available_stats.index("STR"))
                        # Breaks the loop. reprinting the list of remaining stats and hte next acore to assign
                        break
                    case "DEX":
                        new_stats["DEX"] = score
                        available_stats.pop(available_stats.index("DEX"))
                        break
                    case "CON":
                        new_stats["CON"] = score
                        available_stats.pop(available_stats.index("CON"))
                        break
                    case "INT":
                        new_stats["INT"] = score
                        available_stats.pop(available_stats.index("INT"))
                        break
                    case "WIS":
                        new_stats["WIS"] = score
                        available_stats.pop(available_stats.index("WIS"))
                        break
                    case "CHA":
                        new_stats["CHA"] = score
                        available_stats.pop(available_stats.index("CHA"))
                        break
                    case _:
                        print("Sorry, that is not recognised as a stat. Please try again")
    return new_stats