class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance=amount+self.balance
        return self.balance

    def withdrawal(self,amount):
        self.amount=amount
        self.balance=self.balance-self.amount
        return self.balance

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,title,balance,interest):
        super().__init__(title,balance)
        self.interestRate=interest

    def interestAmount(self):
        interest_amount=(self.interestRate*self.balance)/100
        return interest_amount

demo1=SavingsAccount('Dinesh', 5000, 5)
print(demo1.deposit(1000))
data=demo1.get_balance()
print(data)
print(demo1.withdrawal(3))