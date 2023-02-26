## Fawwaz Anrico Purnomo 215150301111019
class Akun:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction = []

    def withdraw_money(self, amount):
        if amount < self.balance:
            self.transaction = [f'Withdrawl = ${amount}']
            self.balance -= amount
        else:
            print('Insufficient amount')
    
    
    def deposit_money(self, amount):

        self.transaction = [f'Deposit = ${amount}']
        self.balance += amount
       

class CheckingAccount(Akun):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def write_check(self, amount):
        if amount <= self.balance:
    
            self.transaction = [f'Withdrawl: ${amount}', f'Check: ${amount}' ]
            self.balance -= amount
        else:
            print('Insufficient amount')

class SavingAccount(Akun):
    def __init__(self, account_number, balance, interest):
        super().__init__(account_number, balance)
        self.interest = interest
        self.total_interest = 0

    def calculate_interest(self):
        self.total_interest += self.balance*self.interest
        self.transaction = ["Deposit: ${}".format(self.total_interest), 'Interest: ${}'.format(self.total_interest)]
        self.balance += self.balance*self.interest




def main():
  checking = CheckingAccount("123456", 1000.00)
  saving = SavingAccount("654321", 5000.00, 0.02)


  checking.write_check(100.00)
  checking.deposit_money(100.00)
  saving.calculate_interest()

  print(checking.account_number, checking.balance, checking.transaction)
  print(saving.account_number,saving.balance,saving.transaction)

if __name__ == "__main__":
    main()
