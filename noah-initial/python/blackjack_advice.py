"""
Blackjack Advice
By:Noah Wallis

"""

card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


card_integer_values = []

while True:
    try:
        card_one = input("What is your first card?: ").upper()
        card_integer_values.append(card_values[card_one])
        
        card_two = input("What is your second card?: ").upper()
        card_integer_values.append(card_values[card_two])
        
        card_three = input("What is your third card?: ").upper()
        card_integer_values.append(card_values[card_three])
        break

    except KeyError:
        print("That is not a valid card, try again!")
        

sum_of_cards = card_integer_values[0] + card_integer_values[1] + card_integer_values[2]
print(f"The total number of points you have is {sum_of_cards}!")


if sum_of_cards < 17:
    print("You are advised to hit!")

elif sum_of_cards >= 17 and sum_of_cards < 20:
    print("You are advised to stay!")

elif sum_of_cards == 21:
    print("You have blackjack!")

else:
    print("You already busted!")
