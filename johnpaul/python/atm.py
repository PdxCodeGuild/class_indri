#ATM with a class containing two attributes: a balance and an interest rate. 
# A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
# The REPL below calls the methods of the class to simulate an ATM.


class ATM:
    
    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self._balance = 0
        self.__interest = 0.1
        
    
        
    def deposit(self, amount):
        # add the given amount to the balance
        self._balance += amount
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if self._balance >= amount:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self._balance -= amount
        return self._balance
    
    def balance(self):
        # return the account balance
        return self._balance  
        
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        return self._balance * self.__interest


# Part 2: Have the ATM maintain a list of transactions
# Add a new method 
    def print_transactions(self, transaction):
        transaction = []
        if command == "deposit":
            transaction.append(f'User deposited: {atm.deposit}')
            return transaction
        elif command == "withdraw":
            transaction.append(f'User withdrew: {atm.withdraw}')
            return transaction



atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
    elif command == 'print transaction':
        transaction = input('Which transaction would you like to print (deposit or withdraw)? ')
        if transaction == 'deposit':
            atm.print_transactions(transaction)
            print(f'User deposited: ${transaction}')
        elif transaction == 'withdraw':
            atm.print_transactions(transaction)
            print(f'User withdrew ${transaction}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
