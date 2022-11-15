class ATM:

    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.account = 0
        self.interest_rate = 0.1
        self.transactions = []
    
    def balance(self):
        # return the account balance
        return self.account
       
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.account += amount
        self.transactions.append(f"user deposited ${amount}")
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if amount <= self.account:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.account -= amount
        self.transactions.append(f"user withdrew ${amount}")
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        interest = self.account * 0.1
        return interest
    
    def print_transactions(self):
        #Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions.
        return self.transactions

        

atm = ATM() # create an instance of our class
print('Welcome to the ATM!')
while True:
    command = input('Enter a command:\n')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}.')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit?\n'))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}.')
    elif command == 'withdraw':
        amount = float(input('How much would you like?\n'))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}.')
        else:
            print('Insufficient funds.')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest.')
    elif command == 'transactions':
        print('Here are your recent transactions:\n')
        for transaction in atm.transactions:
            print(transaction)
        
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized.')