'''
LCR Simulator
LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.
'''

import random
# Create a list of possible outcomes.
dice = ["dot", "dot", "dot", "L", "R", "C"]
# Create empty list for players.
players = []
# Center pot counter starting at 0
center_pot = 0
# Create a list of dictionaries with player information. Each player gets 3 chips.
while True:
    profile = {

        "name": "",
        "chips": 3

    }
# Taking player names and adding them to profile
    profile["name"] = input("Enter player names or type 'done' when finished: ")
# If user types done game begins with all entered profiles
    if profile["name"] == "done":
        break
# Continue to create player profiles
    else:
        players.append(profile)

# Generate a random choice from dice list.
def roll():
    random_roll = random.choice(dice)
    return random_roll
            
w = True
while w == True:
    for i in range(len(players)): # For 'i' in range of players, this is each player taking their turn. 
        # If chips in pot in addition to the last players tokens equals all tokens in game, that player wins.
        if (center_pot + players[i]["chips"]) == (len(players) * 3):
            print(f"{players[i]['name']} has won!")
            w = False
            break
        num_rolls = min(players[i]["chips"], 3)
        for x in range(num_rolls): # Rolls dice according to how many chips a player has, with a maximum of 3 rolls
            result = roll()   

            if result == "C":
                center_pot += 1
                players[i]["chips"] -= 1
            elif result == "L":
                players[i]["chips"] -= 1
                players[i - 1]["chips"] += 1
            elif result == "R":
                players[i]["chips"] -= 1
                # Check if there's a player next in the list
                try: 
                    players[i + 1]["chips"] += 1
                # If no player next in the list return to first player in the list
                except:
                    players[0]["chips"] += 1

            


