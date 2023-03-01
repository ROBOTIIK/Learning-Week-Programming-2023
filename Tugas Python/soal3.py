#soal3

class Account:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount:.2f}")
        else:
            print("Insufficient funds.")

class CheckingAccount(Account):
    def _init_(self, account_number, balance):
        super()._init_(account_number, balance)
        self.transactions = []

    def write_check(self, amount):
        self.balance -= amount
        self.transactions.append(f"Check: ${amount:.2f}")

class SavingsAccount(Account):
    def _init_(self, account_number, balance, interest_rate):
        super()._init_(account_number, balance)
        self.interest_rate = interest_rate
        self.transactions = []

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.transactions.append(f"Interest: ${interest:.2f}")
        
checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()
        

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)