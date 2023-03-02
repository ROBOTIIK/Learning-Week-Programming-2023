class CheckingAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def write_check(self):
        return self.balance - self.a
class SavingsAccount:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
CheckingAccount.write_check(100.00)

CheckingAccount = CheckingAccount("123456", 1000.00)
SavingsAccount = SavingsAccount("654321", 5000.00, 0.02)
print(CheckingAccount.account_number, CheckingAccount.balance, CheckingAccount.write_check)
print(SavingsAccount.account_number, SavingsAccount.balance, SavingsAccount.interest_rate)