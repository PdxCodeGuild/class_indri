"""
lab 14: pick 6 - lottery simulator
"""

import random

payout = {0, 4, 7, 100, 50000, 1000000, 25000000}
    # payout = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

balance=0
earnings=0
expenses=0

def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket


def calculate_payout(winning, ticket):
    """
    calculates payout based on number of matches between a ticket and the winning ticket

    :winning: list of six ints
    :ticket: list of six ints
    returns int of dollars won based on number of matches
    """
   
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1

    if matches > 3:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    # return payout[matches]

    # # using comprehensions
    # matches = [winning[i] for i in range(len(winning)) if winning[i] == ticket[i]]
    # # print('matches:', matches)
    # # print('num matches:', len(matches))
    # return payout[len(matches)]


def play100k():
    # 1. Generate a list of 6 random numbers representing the winning ticket
    # 2. Start your balance at 0

    
    
    # 7. Add to your balance the winnings from your matches
    # 8. After the loop, print the final balance

    winning = pick6()
    balance = 0

    # 3. Loop 100,000 times, for each loop:
    # 4. Generate a list of 6 random numbers representing the ticket
    for i in range(100000):
        ticket = pick6()
        # 5. Subtract 2 from your balance (you bought a ticket)
        balance -= 2
        # 6. Find how many numbers match
        matches = calculate_payout(winning, ticket)
         # 7. Add to your balance the winnings from your matches
        winnings= payout[matches]
        balance= balance + winnings
        earnings= earnings + winnings

ROI=(earnings - expenses)/expenses
 # 8. After the loop, print the final balance
print(balance)
print(ROI)