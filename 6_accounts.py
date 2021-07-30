
#$ Base class
class Account:
    def __init__(self, an,hn,balance):
        #! fields
        self.account_number = an
        self.holder_name = hn
        self.balance = balance

    #~ Methods
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def printMe(self):
        print(self.account_number, self.holder_name, self.balance)

class SavingsAccount(Account):
    pass
a = Account(1, "Pritesh", 1000000)
a.deposit(10000)
a.printMe()
a.withdraw(100)
