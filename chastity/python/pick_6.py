# Pick 6 lottery simulator Lab
import random
import time

# Generate a list of 6 random numbers representing the winning tickets
def get_pick6():
    winning=[]
    size=6 # constant that stores size of list
    for i in range(size): # a loop that runs 6 times
        winning.append(random.randint(1,99)) # appendiing a generated random number to the list
    return winning # return winning numbers


# Start your balance at 0
def calculate_payout(winning, ticket):
    """
    calculates payout based on number of matches between a ticket and the winning ticket
    :winning: list of six ints
    :ticket: list of six ints
    returns int of dollars won based on number of matches
    """
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1 # payout = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
        
    if matches > 3:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    return payout[matches]
    
# Loop 100,000 times, for each loop:
def play100k():
    winning = get_pick6()
    balance = 0

    for i in range(100000):
        ticket = get_pick6()
        balance -= 2
        payout = calculate_payout(winning, ticket)
        balance += payout

    print('balance:', balance)
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches

# After the loop, print the final balance
