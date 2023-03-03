class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaksi = []

    # tambah uang
    def deposit(self, amount):
        self.balance += amount
        self.transaksi.append(f"Deposit: ${amount:.2f}")
    
    # ambil uwang
    def withdrawal(self, amount):
        if self.balance >= amount :
            self.balance -= amount
            self.transaksi.append(f"Withdrawal: ${amount:.2f}")
        else :
            print("Insufficient balance!")

# rekening giro
class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    # tulis check
    def write_check(self, amount):
        self.withdrawal(amount)
        self.transaksi.append(f"Check: ${amount:.2f}")

#rekening tabungan 
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate #bunga

    # hitung bunga
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.transaksi.append(f"Interest: ${interest:.2f}")
        

checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transaksi)
print(savings.account_number, savings.balance, savings.transaksi)
