"""
    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000
"""
import random

def pick6():
    # ticket = []
    # i = 0
    # while i < 6:
    #     ticket.append(random.randint(1, 99))
    #     i += 1

    # return ticket

    return random.choices(range(1, 99), k=6)

random.choices

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1

    return matches

payouts = {
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000
}

results = {}


# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = pick6()

# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:
ticket = []
ticket_counter = 0
while ticket_counter < 100_000:

    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
    ticket_counter += 1

    # Subtract 2 from your balance (you bought a ticket)
    balance -= 2

    # Find how many numbers match
    matches = num_matches(winning_ticket, ticket)

    # Add to your balance the winnings from your matches
    balance += payouts.get(matches, 0)

    # Add to results dictionary
    if matches not in results:
        results[matches] = 1
    else:
        results[matches] += 1

# After the loop, print the final balance
print(f"Congrats! You won ${balance}")
print(results)