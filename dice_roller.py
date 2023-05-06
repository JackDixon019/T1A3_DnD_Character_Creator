from random import randint
from libraries import default_stats
import colored
from colored import stylize

info = colored.fg("green")
options = colored.fg(218)
error = colored.fg("red")
variable = colored.fg("yellow")


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
    print(stylize("\nYour available rolls are:\n", info))
    for i in available_scores:
        print(stylize(i, variable))
    # While there are values in the list of stats available to edit:
    while available_stats != []:
        for score in available_scores:
            print(stylize(f"\nThe next score to assign is: ", info) + stylize(f"{score}\n", variable))
            print(stylize(f"The available stats to assign a score to are:", info))
            for stat in available_stats:
                print(stylize(f'{stat}', options))
            while True:
                # allows the user to input a value.
                chosen_stat = input(stylize(f"Please enter a stat you would like to assign the score", info) + stylize(f" {score}:\n", variable)).upper()
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
                        print(stylize("Sorry, that is not recognised as a stat. Please try again", error))
    return new_stats