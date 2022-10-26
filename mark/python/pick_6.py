'''
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match.

Calculate your net winnings (the sum of all expenses and earnings).

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
from audioop import add
import random

# pick 6 number generator
def pick6(numbers):
    '''pick6 number generator'''
    while len(numbers) < 6:
        numbers.append(random.randint(1,100))
    return numbers

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []
pick6(winning_ticket)

# Start your balance at 0
user_balance = 0

# tracking expenditures & earnings 
expenses = []
earnings = []

# Loop 100,000 times
for x in range(100000):
    
    # Generate a list of 6 random numbers representing the ticket
    user_ticket = []
    pick6(user_ticket)

    # Subtract 2 from your balance (you bought a ticket, expenditure)
    expenses.append(int(-2))

    # Find how many numbers match from the user ticket against the winning ticket (assume none, add 1 for every match)
    matches = 0
    for i in range(len(user_ticket)):    
        if user_ticket[i] == winning_ticket[i]:
            matches = matches + 1
    # print("matches: ", matches)

    # add prize winnings to earnings bucket
    if matches == 1:
        earnings.append(int(4))
    elif matches == 2:
        earnings.append(int(7))
    elif matches == 3:
        earnings.append(int(100))
    elif matches == 4:
        earnings.append(int(50000))
    elif matches == 5:
        earnings.append(int(1000000))
    elif matches == 6:
        earnings.append(int(25000000))

# calculate total expenses and earnings
total_expenses = sum(expenses)
total_earnings = sum(earnings)

# After the loop, print the final balance
user_balance = total_expenses - total_earnings
print("final balance: ", user_balance)

# Display total earnings, total expneses & the return on investment
print("Total expenses: ", total_expenses, "\nTotal earnings: ", total_earnings)
roy = (total_earnings - total_expenses)/(total_expenses)
print("ROI: ", roy)
