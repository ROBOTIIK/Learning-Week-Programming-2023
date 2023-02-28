class Bank :
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def withdraw(self, money):
        if(self.balance - money >= 0):
            self.balance -= money
            self.transactions.append(f"Withdrawal: ${money:.2f}")
            return True
        else:
            print("Failed to withdraw the money")
            return False

    def deposit(self, money):
        self.balance += money
        self.transactions.append(f"Deposit: ${money:.2f}")



class CheckingAccount(Bank):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)


    def write_check(self, money):
        if(self.withdraw(money)):
            self.transactions.append(f"Check: ${money:.2f}")



class SavingsAccount(Bank):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_value = self.balance * self.interest_rate
        self.deposit(interest_value)
        self.transactions.append(f"Interest: ${interest_value:.2f}")


checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)