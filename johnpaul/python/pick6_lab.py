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
# -------------------------------------------------------------------------------------------#


import random

# Generate a list of 6 random numbers representing the winning tickets


def pick6():
    winning_tickets = []
    i = 0
    while i < 6:
        winning_tickets.append(random.randint(1, 99))
        i += 1
    return winning_tickets


winning = pick6()  # winning ticket

print(winning)
print()

# #-------------------------------------------------------------------------------------------#
# # Looping 100,000 times ## Generate a list of 6 random numbers representing the ticket


def ticket():
    my_ticket = 0
    random_ticket = []  # ---------------------- my your ticket at 0
    while my_ticket < 100000:
        ticket = pick6()
        random_ticket.append(ticket)
        my_ticket += 1
    return random_ticket


result = ticket()
# print(result)
# #-------------------------------------------------------------------------------------------#
beginning_balance = 0

for nums in range(len(result)):
    # print(nums)
    matched = 0
    for item in range(len(result[nums])):
        # print(item, result[nums][item])
        matching_ticket = winning[item] == result[item]
        # print(matching_ticket)
        # while matching_ticket == "False" or matching_ticket == "True":
        if matching_ticket == True:
             matched += 1
            #  print(matched)

    if matched == 1:
        beginning_balance += 4
    elif matched == 2:
        beginning_balance += 7
    elif matched == 3:
        beginning_balance += 100
    elif matched == 4:
        beginning_balance += 50000
    elif matched == 5:
        beginning_balance += 1000000
    elif matched == 6:
        beginning_balance += 25000000
    # print(matched)
    # print(beginning_balance)

print("you played",nums+1, " tickets")
ticket_cost = (-2 * (nums+1))
earnings = beginning_balance
print('you earned: ', earnings)
print('you owe:', ticket_cost)


# # #-------------------------------------------------------------------------------------------#
# Calculate return on investment
ROI = (f' {(((earnings - ticket_cost) / ticket_cost)) * 100}%')
print('your ROI:', ROI)
