class Account:
    def __init__ (self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def cash_withdrawal(self, money):
        if self.balance > money:
            self.balance -= money
            self.transactions = [f'Withdraw : ${money}']
        else:
            print("Insufficient balance")
    
    def save(self, money):
        if self.balance <= money:
            self.balance += money
            self.transactions = [f'Deposit : ${money}']

class CheckingAccount(Account):
    def __init__ (self, account_number, balance):
        super().__init__(account_number, balance)
        self.transactions = []

    def write_check (self, money):
        if self.balance > money:
            self.balance -= money
            self.transactions = [f'Withdraw: ${money}', f'Deposit: ${money}']
            return self.balance
        else:
            print("Insufficient balance")
        
class SavingsAccount(Account):
    def __init__ (self, account_number, balance, calculateinterest):
        super().__init__(account_number, balance)
        self.calculateinterest = calculateinterest
        self.transactions = []
        self.interest_yield = 0

    def calculate_interest(self):
            self.interest_yield += self.calculateinterest * self.balance
            self.transactions = [f'Deposit : ${self.interest_yield}', f'Interest : ${self.interest_yield}']
            self.balance += self.interest_yield

checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)
