class Savings:
    def __init__(self, account_number, balance, interest, transactions=0):
        self.account_number = account_number
        self.balance = float(balance)
        self.interest = float(interest)
        self.transactions = transactions

    def deposit(self, money):
        self.balance = self.balance + float(money)
        self.transactions = f"['Deposit: ${float(money)}, 'Savings: ${self.balance}']"

    def Withdraw(self, money):
        self.balance = self.balance - float(money)
        self.transactions = f"['Withdrawal: ${float(money)}, 'Savings: ${self.balance}']"

    def calculate_interest(self):
        interest_rate = self.balance * self.interest
        self.balance = self.balance + interest_rate
        self.transactions = f"['Deposit: ${interest_rate}, 'Interest: ${interest_rate}']"

class SavingsAccount(Savings):
    def __init__(self, account_number, balance, interest):
        Savings.__init__(self, account_number, balance, interest)

class Checking:
    def __init__(self, account_number, balance, transactions=None):
        self.account_number = account_number
        self.balance = float (balance)
        self.transactions = transactions

    def deposit(self, money):
        self.balance = self.balance + float(money)
        self.transactions = f"['Deposit: ${float(money)}, 'Savings: ${self.balance}']"

    def Withdraw(self, money):
        self.balance = self.balance - float(money)
        self.transactions = f"['Withdrawal: ${float(money)}, 'Savings: ${self.balance}']"

    def write_check(self, money):
        self.balance = self.balance - money
        self.transactions = f"['Withdrawal: ${money}, 'Check: ${money}']"

class CheckingAccount(Checking):
    def __init__(self, account_number, balance):
        Checking.__init__(self, account_number, balance)


checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)