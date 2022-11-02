"""
Pick 6 lottery generator
By: Noah Wallis

"""
import random


def pick_6():
    generated_numbers = []
    i = 0
    while i < 6:
        generated_numbers.append(random.randint(1,99))
        i = i + 1
    return generated_numbers


def num_matches(winning_numbers,ticket):
    for i in range(len(winning_numbers)):
        print(winning_numbers[i] == ticket[i]) #start here tomorrow

        
# Generate a list of 6 random numbers representing the winning tickets
winning_numbers = pick_6()
print(winning_numbers)

# Start your balance at 0

balance = 0

# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)

ticket = []
ticket_counter = 0

while ticket_counter < 100000:
    ticket = pick_6()
    ticket_counter = ticket_counter + 1
    balance = balance - 2


#find how many numbers match


# Add to your balance the winnings from your matches



# After the loop, print the final balance
print(f"Your final balance after 100,000 tickets played is {balance}!")