class account:
    
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance=balance
    
class CheckingAccount(account):
    
    def __init__(self, account_number, balance, transactions=[]):
        account.__init__(self, account_number, balance)
        self.transactions=transactions
        
    def write_check(self, money):
        self.balance-=money
        self.transactions.extend((f'Withdrawal: ${money}', f'Check: ${money}'))
    
class SavingsAccount(account):
    
    def __init__(self, account_number, balance, interest, transactions=[]):
        account.__init__(self, account_number, balance)
        self.interest=interest
        self.transactions=transactions
        
    def calculate_interest(self):
        total_interest=self.balance*self.interest
        self.balance+=total_interest
        self.transactions.extend((f'Withdrawal: {total_interest}', f'Interest: ${total_interest}'))
        
checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)