class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def write_check(self, amount):
        self.balance = self.balance - amount
        self.transactions.append(f"Withdrawal: ${amount}")
        self.transactions.append(f"check: ${amount}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest):
        super().__init__(account_number, balance)
        self.interest = interest

    def calculate_interest(self):
        bunga = self.interest * self.balance
        self.balance = self.balance + bunga
        self.transactions.append(f"Deposit: ${bunga}")
        self.transactions.append(f"Interest: ${bunga}")

checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)