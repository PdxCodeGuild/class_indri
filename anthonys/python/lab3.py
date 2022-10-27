import random

match_cash={
0 : 0,
1 : 4,
2 : 7,
3 : 100,
4 : 50000,
5 : 1000000,
6 : 25000000,
}

balance=0
earnings=0
expenses=0
def pick6():
    lottery_numbers=[]
    for number in range(0, 6):
        number=random.randint(1,90)
        lottery_numbers.append(number)
    return lottery_numbers

winning_ticket=pick6()


def num_matches(winning,ticket):
    match=0
    for i in range(len(winning)):
        if winning[i]==ticket[i]:
            match+=1
    return match

for i in range(100000):
# Generate a list of 6 random numbers representing the ticket
    my_ticket=pick6()
# Subtract 2 from your balance (you bought a ticket)
    balance-=2
    expenses+=2
# Find how many numbers match
    matches=num_matches(winning_ticket, my_ticket)
# Add to your balance the winnings from your matches
    winnings=match_cash[matches]
    balance= balance + winnings
    earnings= earnings + winnings

ROI=(earnings - expenses)/expenses
# After the loop, print the final balance
print(balance)
print(ROI)
