import random

# pick 6 number generator
def pick6(numbers):
    '''pick6 number generator'''
    while len(numbers) < 6:
        numbers.append(random.randint(1,100))
    return numbers

# compare two lists and add to a counter when a matching index is found.
def num_matches(winning_ticket, user_ticket):
    matches = 0
    for i in range(len(user_ticket)):    
        if user_ticket[i] == winning_ticket[i]:
            matches += 1
    return matches

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []
pick6(winning_ticket)

# Start your balance at 0
user_balance = 0

# tracking expenditures & earnings 
expenses = []
earnings = []

for x in range(100000):
    
    # Generate a list of 6 random numbers representing the ticket
    user_ticket = []
    pick6(user_ticket)
    # print(winning_ticket) #testing comparison
    # print(user_ticket)

    # Subtract 2 from your balance (you bought a ticket, expenditure)
    expenses.append(int(-2))

    # Find how many numbers match from the user ticket against the winning ticket
    chicken_dinner = num_matches(winning_ticket, user_ticket)
    # print(chicken_dinner) #testing matchs

    # add prize winnings to earnings bucket
    if chicken_dinner == 1:
        earnings.append(int(4))
    elif chicken_dinner == 2:
        earnings.append(int(7))
    elif chicken_dinner == 3:
        earnings.append(int(100))
    elif chicken_dinner == 4:
        earnings.append(int(50000))
    elif chicken_dinner == 5:
        earnings.append(int(1000000))
    elif chicken_dinner == 6:
        earnings.append(int(25000000))
    # print(sum(earnings)) #testing earnings

# Sum of expenditures & earnings
total_expenses = sum(expenses)
total_earnings = sum(earnings)


# # After the loop, print the final balance
user_balance = total_earnings - abs(total_expenses) #absolute value expenses used for math
print("final balance: ", user_balance)

# # Display total earnings, total expneses & the return on investment
print("Total expenses: ", total_expenses, "\nTotal earnings: ", total_earnings)
roy = -(total_earnings - abs(total_expenses))/(total_expenses)
print("ROI: ", roy)