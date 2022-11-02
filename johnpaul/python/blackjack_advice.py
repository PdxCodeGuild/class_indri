"""
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. 
At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""

#########################################################################

print("\nBlackjack Advice")
print("===============================================")
print("""
\nAvailable card Input: 
-----------------------
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K
""")

def get_user_card(prompt):
     while True:
         try:
             card_input = input(prompt).upper()
             card_values[card_input]
             break
         except KeyError:
             print("That is not a valid card, try again")
     return card_values[card_input] # Returning the card input value help us avoid using variables in line 51

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


score = get_user_card("What is your first card? ") + get_user_card("What is your second card? ") + get_user_card("What is your third card? ")

 # if score is less than 17, advice them to 'hit'
if score < 17:
     print("You are advised to hit.")

 # if score is between 17 and 21, advice them to stay
elif score >= 17 and score < 21:
     print("You are advised to stay.")

 # if score is exactly 21, advise blackjack 
elif score == 21:
     print("Blackjack!")

 # otherwise, they bust
else:
     print("Bust... :(")