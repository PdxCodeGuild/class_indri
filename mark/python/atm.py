'''
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
The REPL below calls the methods of the class to simulate an ATM.
'''
transaction_list = []
class ATM:    
    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.user_balance = 0
        self.interest = 0.1
    
    def balance(self):
        # return the account balance
        return self.user_balance
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.user_balance = self.user_balance + float(amount)
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if self.user_balance - amount < 0:
            return False
        else:
            return True
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.user_balance = self.user_balance - float(amount)

    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        interest = self.user_balance * self.interest
        # return the amount of interest added
        return interest
        
    # Add a new method print_transactions() to your class for printing out the list of transactions.'''
    def print_transactions(self):
        return transaction_list

atm = ATM() # create an instance of our class
# Have the ATM maintain a list of transactions. 
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        transaction_list.append(f"user deposited {amount}.") # add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount):
            transaction_list.append(f"user withdrew {amount}.")
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        transaction_list.append(f"user earned {amount} in interest.")
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
    
    elif command == 'transactions':
        print(atm.print_transactions())
    
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('transactions - get all transactions')
        print('exit         - exit the program')
    
    elif command == 'exit':
        break
    
    else:
        print('Command not recognized')
