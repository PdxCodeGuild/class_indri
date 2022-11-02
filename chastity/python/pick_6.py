# Pick 6 lottery simulator Lab
import random

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

    # # using comprehensions
    # matches = [winning[i] for i in range(len(winning)) if winning[i] == ticket[i]]
    # # print('matches:', matches)
    # # print('num matches:', len(matches))
    # return payout[len(matches)]
    
# Loop 100,000 times, for each loop:
def play100k():
    # 1. Generate a list of 6 random numbers representing the winning ticket
    winning = get_pick6()
    # 2. Start your balance at 0
    balance = 0
    # 3. Loop 100,000 times, for each loop:
    # 4. Generate a list of 6 random numbers representing the ticket
    for i in range(100000):
        ticket = get_pick6()
        # 5. Subtract 2 from your balance (you bought a ticket)
        balance -= 2
        # 6. Find how many numbers match
        payout = calculate_payout(winning, ticket)
         # 7. Add to your balance the winnings from your matches
        balance += payout
    print('balance:', balance)

play100k()


# 8. After the loop, print the final balance
# ROI=(earnings - expenses)/expenses
# print(balance)
# print(ROI)