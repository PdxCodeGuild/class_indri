'''
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
Write the following functions and use them in the code:

pick6(): Generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Return the list
num_matches(winning, ticket): Return the number of matches between the winning numbers and the ticket.
'''
import random

# pick 6 number generator
def pick6(numbers):
    '''pick6 number generator'''
    while len(numbers) < 6:
        numbers.append(random.randint(1,100))
    return numbers

# add to balance based on results of comparing winning ticket numbers to user ticket numbers
# def prizes(list):

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []
pick6(winning_ticket)

print("winning_ticket: ", winning_ticket)

# Start your balance at 0
user_balance = 0
print("user_balance: ", user_balance)

# # Loop 100,000 times, for each loop:
for x in range(3):
# # Generate a list of 6 random numbers representing the ticket
    user_ticket = winning_ticket
    # pick6(user_ticket)

    print("user_ticket: ", user_ticket)
# # Subtract 2 from your balance (you bought a ticket)
    user_balance = user_balance - 2
    print ("user_balance: ", user_balance)

# Find how many numbers match 
    matches = 0
    for i in range(len(user_ticket)):    
        print(len(user_ticket[i] == winning_ticket[i]))




#     print(len(matches))
# # # Add to your balance the winnings from your matches
#     if matches == 1:
#         user_balance = user_balance + 4

# print(user_balance)

#     if len(winner_winner(user_ticket)) == 1:
#         user_balance + 4 == user_balance
#     # elif len(winner_winner(user_ticket)) == 2:
#     #     user_balance == user_balance + 7
#     # elif len(winner_winner(user_ticket)) == 3:
#     #     user_balance == user_balance + 100
#     # elif len(winner_winner(user_ticket)) == 4:
#     #     user_balance == user_balance + 50000
#     # elif len(winner_winner(user_ticket)) == 5:
#     #     user_balance == user_balance + 1000000
#     # elif len(winner_winner(user_ticket)) == 6:
#     #     user_balance == user_balance + 25000000
#     print(user_balance)

# # After the loop, print the final balance
# print(user_balance)