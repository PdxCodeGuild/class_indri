# Blackjack Advice

# Figure out the point value of each card indicidually
cards = { 
    'A': 1,
    'K': 10,
    'Q': 10,
    'J': 10
}
    
# Ask user for the first three playing cards
player_card1 = input("What's your first card?: ")
player_card2 = input("What's your second card?: ")
player_card3 = input("What's your third card?: ")

# Calculate the cards total
card_value = int(player_card1 + player_card2 + player_card3)

# Advise using the rules 
def calculate_card_play(card_value: int):
    card_value == ""
    if (card_value >= 17) or (card_value < 21):
        print("{card_value} Stay")
    elif card_value < 17:
        print("{card_value} Hit")
    elif card_value == 21:
        print("{card_value} Blackjack!")
    else:
        print("{card_value} Already Busted")

        

    

