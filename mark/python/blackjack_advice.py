# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 


# Ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 

first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")
# Store cards in a list for later recall
user_hand = [first_card, second_card, third_card]


# Dictionary containing value of each card individually. 
# Number cards are worth their number, all face cards are worth 10. 
card_value = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "10" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "1" : 1,
    "A" : 1
}


# Calculate the sum of the three cards to get the total point value
score = card_value[first_card] + card_value[second_card] + card_value[third_card]


# check for Aces and add points so long as it won't cause you to lose 
while "A" in user_hand and score <= 12:
    # score is added with ace = 1, add 9 to get 10 points.
    # Aces are only counted as 10 points one at a time.
    score = score + 9
    # remove one ace from the user's hand after they get points for it
    user_hand.remove("A")
    # print(user_hand) #test #success!

# print(score) #test # success!


# Create a function that returns advice
def Blackjack(advice):
    '''
    returns blackjack advice based on total score
    ''' 
    # Less than 17, advise to "Hit"
    if score < 17:
        advice = "Hit"
    # Greater than or equal to 17, but less than 21, advise to "Stay"
    elif score >=17 and score <21:
        advice = "Stay"
    # Exactly 21, advise "Blackjack!"
    elif score == 21:
        advice = "Blackjack!"
    # Over 21, advise "Already Busted"
    elif score >21:
        advice = "Bust!"

    return advice

# Print out the current total point value and the advice.
print(score, Blackjack(score))








