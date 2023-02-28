class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def withdrawal(self, amount):
        if amount < 0:
            return print("Withdrawal amount can't be less than 0")
        elif amount > self.balance:
            return print("Balance is not sufficient")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount:.2f}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount:.2f}")

class CheckingAccount(BankAccount):
    def write_check(self, amount):
        self.withdrawal(amount)
        if self.balance >= amount and amount >= 0:
            self.transactions.append(f"Check: ${amount:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest):
        self.interest = interest
        BankAccount.__init__(self, account_number, balance)

    def calculate_interest(self):
        interest = self.interest * self.balance
        self.deposit(interest)
        self.transactions.append(f"Interest: ${interest:.2f}")

checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)        