
#$ Account is base class
#~ Saving account - Derived class
#* Withdraw should allowed upto 500 min balance

#~ Current Account - Derived class
#* withdraw should allow upto -10000 balance


class Account:
    def __init__(self, name, balance, acc_number ):
        self.account_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def printMe(self):
        print(self.account_number, self.name, self.balance)

    def print(self):
        print("this is print")

class SavingAccount(Account):
    def withdraw(self, amount):
        if((self.balance - amount) < 500):
            print("Not allowed to withdraw from Savings account.")
        else:
            self.balance -= amount
            print("Amount withdrawal successfull from savings account.")

class CurrentAccount(Account):
    def withdraw(self, amount):
        if((self.balance - amount)> -10000):
            self.balance -= amount
            print("Amount withdrawal successfull from savings account.")
        else:
            print("Not allowed to withdraw minimum balance violation for current account")


if __name__ == '__main__':
    savingAccount = SavingAccount('Ram', 3000, 1)
    print("withdraw to exhaust minimum balance")
    savingAccount.withdraw(2700)
    print("Updated Savings Account")
    savingAccount.printMe()

    print("withdraw More than minimum balance")
    savingAccount.withdraw(2200)
    print("Updated Savings Account after withdrawal")
    savingAccount.printMe()
    