# banking.py

class BankAccount:
    
    
    def __init__(self):
        self.balance = 0
        

    def deposit(self, amount):
        self.balance = amount + self.balance
       # return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
    
       # return self.balance

    def transfer(self, amount, account):
        if self.balance > amount:
            account.balance = amount + account.balance
            self.balance = self.balance - amount
        

    
