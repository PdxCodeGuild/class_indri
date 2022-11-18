'''

Blackjack Advice Lab 02 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''
    
# Ask user for three playing cards
player_card1 = input("What's your first card?: ")
player_card2 = input("What's your second card?: ")
player_card3 = input("What's your third card?: ")

# Calculate the cards total
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

hand_value = card_values[player_card1] + card_values[player_card2] + card_values[player_card3]

# Advise using the rules 
# class hand(object):
hand_value == ""
if (hand_value >= 17) or (hand_value < 21):
    print(f"{hand_value} Stay")
elif hand_value < 17:
    print(f"{hand_value} Hit")
elif hand_value == 21:
    print(f"{hand_value} Blackjack!")
else:

    print(f"{hand_value} Already Busted")
