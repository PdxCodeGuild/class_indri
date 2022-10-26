"""
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

"""
import random
#STEPS
## Generate a list of 6 random numbers representing the winning tickets
def pick6():
    winning_tickets = []
    choices = range(1, 100)
    for x in range(6):
        winning_tickets.append(random.choices(choices, k = 6))
        print(winning_tickets)
    
pick6()

def num_matches():
   comp_tickets = []
   tickect_choices = range(1, 100)
   for x in range(6):
        comp_tickets.append(random.choices(tickect_choices, k = 6))
        print(comp_tickets)

num_matches()
#--------------------------------------------------------------------------------------------------------------------------------------#
## Start your balance at 0
# Your_balance = 0

#--------------------------------------------------------------------------------------------------------------------------------------#
## Loop 100,000 times, for each loop:
# played_tickets = []
# for x in range(10):
#     if x == random.choices(pick_choice)
#     print(x)
#     x += 1



#--------------------------------------------------------------------------------------------------------------------------------------#


## Generate a list of 6 random numbers representing the ticket

## Subtract 2 from your balance (you bought a ticket)

## Find how many numbers match

## Add to your balance the winnings from your matches

## After the loop, print the final balance