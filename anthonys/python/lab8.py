class ATM:
    transactions=[]
    def __init__(self,current_balance=0):
        self.current_balance=current_balance
        self.interest=.1
        # initialize our class with a balance of 0 and an interest rate of 0.1
        ...

    def balance(self):
        return self.current_balance
        # return the account balance

    def deposit(self, amount):
        #self.balance+=amount 
        self.current_balance=self.current_balance+amount

        # add the given amount to the balance
        ...
    
    def check_withdrawal(self, amount):
        self.current_balance-amount
        if self.current_balance >= 0:
            return True
        else:
            return False
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        ...
    
    def withdraw(self, amount):
        self.current_balance=self.current_balance-amount
        return self.current_balance

        # removes the given amount from the balance and returns it
        ...
    
    def deposit_interest(self):
        self.total_balance=self.current_balance+(self.current_balance * self.interest)
        return self.total_balance
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        ...
    def print_transactions(self):

        print(f'User deposited {amount}')
        print(f'User withdrew {amount}')
        ...

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