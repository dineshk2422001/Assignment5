class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        return(balance,title)


class SavingsAccount(Account):
    def __init__(self,title,balance,interest):
        super().__init__(title,balance)
        self.interestRate=interest
        return self.title,self.balance,self.interestRate


parent=SavingsAccount('Dinesh',5000,5)