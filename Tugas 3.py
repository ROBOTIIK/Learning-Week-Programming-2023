class bank_acc :
    
    def __init__(self, account_number, sum, transactions) -> None:
        self.account_number = account_number
        self.sum = float(sum)
        self.transactions = transactions
    def surplus_sum (self, money):
        self.sum += (float)money
        self.transactions = f"['Deposit: ${float(money)}', 'Savings: ${self.sum}']"
    def minus_sum (self, money):
        if self.sum > money:
            self.sum -= (float)money
            self.transactions = f"['Deposit: ${float(money)}', 'Savings: ${self.sum}']"



