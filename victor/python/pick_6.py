import random

'''
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
'''


def pick6():

    new_ticket = []
    for num in range(0, 6):
        num = random.randint(1, 99)
        new_ticket.append(num)
    return new_ticket
 

balance = 0


def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

# if 1 number matches, you win $4  
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
earnings = 0
counter = 0
while counter <= 100000:
    balance -= 2
    winning = pick6()
    ticket = pick6()
    
    
    if num_matches(winning, ticket) == 1:
            balance += 4
            earnings += 4
    elif num_matches(winning, ticket) == 2:
            balance += 7
            earnings += 7
    elif num_matches(winning, ticket) == 3:
            balance += 100
            earnings += 100
    elif num_matches(winning, ticket) == 4:
            balance += 50000
            earnings += 50000
    elif num_matches(winning, ticket) == 5:
            earnings += 1000000
            balance += 1000000
    elif num_matches(winning, ticket) == 6:
            balance += 25000000
            earnings += 25000000
    counter += 1


ROI = (earnings - 200000) / 200000

print(f"Your final balance is: {balance}")
print(f"You earned ${earnings}, expended $200,000, and had an ROI of {ROI}% ")






