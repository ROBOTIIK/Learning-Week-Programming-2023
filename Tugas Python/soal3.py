class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        self.transactions.append(f"Withdrawal: ${withdraw_amount}")

    def deposit(self, deposit_ammount):
        self.balance += deposit_ammount
        self.transactions.append(f"Deposit: ${deposit_ammount}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def write_check(self, check_amount):
        self.balance -= check_amount
        self.transactions.append(f"Withdrawal: ${check_amount}")
        self.transactions.append(f"Check: ${check_amount}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest):
        super().__init__(account_number, balance)
        self.interest = interest

    def calculate_interest(self):
        interest_amount = self.interest * self.balance
        self.balance += interest_amount

        self.transactions.append(f"Deposit: ${interest_amount}")
        self.transactions.append(f"Interest: ${interest_amount}")


checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)