from random import randint
from libraries import default_stats



def roll_die(number_of_die, dice_to_roll, advantage):
    rolls = []
    for i in range(number_of_die):
        # "rolls" a pseudorandom integer between 1 and 6 --> simulating a d6
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



def assign_score_to_stat(available_scores):
    new_stats = {}
    available_stats = list(default_stats.keys())
    print("\nYour available rolls are:\n")
    for i in available_scores:
        print(i)
    while available_stats != []:
        for score in available_scores:
            print(f"\nThe next score to assign is: {score}\n")
            print(f"The available stats to assign a score to are:")
            for stat in available_stats:
                print(stat)
            while True:
                chosen_stat = input(f"Please enter a stat you would like to assign the score {score}:\n").upper()
                match chosen_stat:
                    case "STR":
                        new_stats["STR"] = score
                        available_stats.pop(available_stats.index("STR"))
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