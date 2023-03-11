class nasabah: 
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit: ${amount:.2f}') 

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.transactions.append(f'Withdrawal: ${amount:.2f}')
            self.balance -= amount



class CheckingAccount(nasabah):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def write_check(self, amount):
        if self.withdraw_money(amount):
            self.transactions.append(f'Check: ${amount:.2f}')

        


class SavingsAccount(nasabah):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

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