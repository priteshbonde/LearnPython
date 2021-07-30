
class Account:
    count =1;
    def __init__(self, name, balance ):
        self.account_number = Account.count
        Account.count += 1
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

    # def __str__(self) -> str:
    #     return f"Account Details Name = {self.name} Account = {self.account_number}"

    def __repr__(self) -> str:
        return f"Account Details Name = {self.name}"

    def __gt__(lhs, rhs):
        return lhs.balance > rhs.balance

    def __eq__(lhs, rhs) -> bool:
        return lhs.balance == rhs.balance

    def __ge__(lhs, rhs):
        return lhs.balance >= rhs.balance
    
    def __lt__(lhs, rhs):
        return lhs.balance>=rhs.balance

    def __le__(lhs, rhs): 
        return lhs.balance<= rhs.balance

    def __ne__(lhs, rhs):
        return lhs.balance != rhs.balance


class SavingAccount(Account):
    def withdraw(self, amount):
        if((self.balance - amount) < 500):
            print("Not allowed to withdraw from Savings account.")
        else:
            self.balance -= amount
            print("Amount withdrawal successfull from savings account.")
    
    def __str__(self):
        return f"Savings account details \n Name = {self.name} Account = {self.account_number}"

class CurrentAccount(Account):
    def withdraw(self, amount):
        if((self.balance - amount)> -10000):
            self.balance -= amount
            print("Amount withdrawal successfull from savings account.")
        else:
            print("Not allowed to withdraw minimum balance violation for current account")
   
    def __str__(self):
        return f"Current Account details \n Name = {self.name} Account = {self.account_number}"

    def __repr__(self) -> str:
        return f"REPR Current account Name = {self.name}"


saving = SavingAccount("John", 10000)
print(str(saving))
sav = SavingAccount("ramesh", 10000)

saving2 = SavingAccount("Ram", 100000)

current = CurrentAccount("Oven story", 100000)
print(str(current))
print(repr(current))

print("Ram's balance greater than John's",  saving2 > saving)
print ("Ram's balance equal to John", saving2 == saving)
print ("ramesh equal to john", sav == sav)
print("Ram greater than equal", saving2 >= saving)
print("Ram less than equal", saving2 <= saving)
print("Ram not equal john", saving2 != saving)
