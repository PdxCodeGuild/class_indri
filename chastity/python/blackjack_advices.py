'''

Blackjack Advice Lab 02 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''


def get_user_card(prompt):
    while True:
        try:
            player_card = input(prompt).upper() # fixes lowercase entry
            card_values[player_card]
            break
        except KeyError:
            print("Thats is not a valid card, try again")
    return player_card #.get(player_card, int(player_card))


# Calculate player score form cards
card_values = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "A": 1,
    
}

# Ask player for 3 cards

        
hand_value = get_user_card("What's your first card?: ") + get_user_card("What's your second card?: ") + get_user_card("What's your thrid card?: ")

# if score is less than 17 advise to 'hit'
# if score is between 17 and 21, advice then to stay
# if score is excatly 21, advice blackjack
# otherwise, they bust
hand_value == ""
if (hand_value >= 17) or (hand_value < 21):
    print(f"{hand_value} Stay")
elif hand_value < 17:
    print(f"{hand_value} Hit")
elif hand_value == 21:
    print(f"{hand_value} Blackjack!")
else:
    print(f"{hand_value} Already Busted")
