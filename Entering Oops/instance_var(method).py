class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction = []
    def deposit(self,amount):
        self.balance += amount
        self.transaction.append(f"Deposit : ${amount}")
        return f"Deposited ${amount} . New Balance : ${self.balance}"
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance -= amount
            self.transaction.append(f"Withdrawal : ${amount}")
            return f"Withdrew ${amount} . New Balance : ${self.balance}"
        return "Insufficient Fund"
    def get_statement(self):
        print(f"Account Holder: {self.owner}")
        print(f"Current Balance : ${self.balance}")
        print("Transactions: ")
        for transaction in self.transactions:
            print(f"      -{transaction}")
account = BankAccount("Ritesh Sahoo",3424)
print(account.deposit(500))
print(account.withdraw(200))
account.get_statement()
