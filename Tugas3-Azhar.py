class akun:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

        self.transaction = []

    def tarik_duit(self, uang):
        if self.balance > uang:
            self.balance -= uang
            self.transaction = [f'Withdraw : ${uang}']
        else:
            print("Saldo tidak mencukupi!!!")
    
    def nabung(self, uang):
        if self.balance <= uang:
            self.balance += uang
            self.transaction = [f'Deposit : ${uang}']

class Checking_Account(akun):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.transaction = []

    def write_check (self, uang):
        if self.balance > uang:
            self.balance -= uang
            self.transaction = [f'Withdraw : ${uang}', f'Deposit : ${uang}']
            return self.balance
        else:
            print("Saldo tidak mencukupi!!!")
    
class Saving_Account(akun):
    def __init__(self, account_number, balance, bunga):
        super().__init__(account_number, balance)
        self.bunga = bunga
        self.transaction = []
        self.hasil_bunga = 0

    def calculate_interest(self):
            self.hasil_bunga += self.bunga * self.balance
            self.transaction = [f'Deposit : ${self.hasil_bunga}', f'Interest : ${self.hasil_bunga}']
            self.balance += self.hasil_bunga

checking = Checking_Account("123456", 1000.00)
savings = Saving_Account("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transaction)
print(savings.account_number, savings.balance, savings.transaction)