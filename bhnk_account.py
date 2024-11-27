class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+= amount
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return amount
        else:
            return amount
    
    def get_balance(self):
        return self.__balance
    
account=BankAccount("Housnah", 1000)
account.deposit(500)
print("balance:", account.get_balance())

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Housnah", 1000)
account.deposit(500)
print("Balance:", account.get_balance())
account.withdraw(300)
print("Balance after withdrawal:", account.get_balance())