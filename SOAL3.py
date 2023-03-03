class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = float(balance)
        self.transactions = []
    def deposit(self, amount):
        self.transactions.append('Deposit: $%.2f' % amount)
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print("Saldo tidak mencukupi")
            return False
        else:
            self.transactions.append('Withdrawal: $%.2f' % amount)
            self.balance -= amount
            return True

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    def write_check(self, amount):
        if(super().withdraw(amount)):
            self.transactions.append('Check: $%.2f' % amount)

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        self.transactions.append('Interest: $%.2f' % (self.balance*self.interest_rate))
        self.deposit(self.balance*self.interest_rate)

checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)