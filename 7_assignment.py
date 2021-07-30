
#! Assignment: Create a Account class with static variable for account number

class Account:

    #? Static Variable can be accessed using Account.count
    count = 1
    def __init__(self, name, balance, min_balance):
        self.holder_name = name
        self.account_number = Account.count
        Account.count+=1
        self.balance = balance
        self.minimum_balance = min_balance

    def print(self):
        print('Account Number ', self.account_number, 'Name ', self.holder_name, 'Balance ', self.balance)

    #? Static method that can be accessed Account.printCount()
    @staticmethod
    def printCount():
        print('Account Count', Account.count)

    def withdraw(self, amount):
        self.balance -= amount

class SavingAccount(Account):
    def __init__(self, name, balance, min_balance):
        super().__init__(name, balance, min_balance)

    def withdraw(self, amount):
        if((self.balance - amount)> self.minimum_balance):
            super().withdraw(amount)
        else:
            print('Withdrawal not allowed for ', self.holder_name)


rajesh = SavingAccount('Rajesh', 100000, 500)
rajesh.print()
rajesh.withdraw(1000)
print('Post withdrawal for rajesh')
rajesh.print()

amit = SavingAccount('Amit', 1000, 1000)
amit.print()
amit.withdraw(100)

Account.printCount()

#? This wont work. Throws error  printCount() takes 0 positional arguments but 1 was given
# amit.printCount()