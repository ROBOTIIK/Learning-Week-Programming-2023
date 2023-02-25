class Details:
    def __init__(self, account_number="<no account_number>", balance="<no balance>", transactions=[]):
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = transactions
        
    def setData(self, account_number, balance, transactions):
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = transactions
        
    def account_number(self):
        return self.__account_number
    
    def balance(self):
        return self.__balance
    
    def transactions(self):
        return self.__transactions


class CheckingAccount(Details):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.__transactions = ["Initial deposit: $" + str(balance)]
        
    def write_check(self, amount):
        if self.balance() - amount < 0:
            print("Error: Insufficient funds")
        else:
            self.__transactions.append("Check: $" + str(amount))
            self.setData(self.account_number(), self.balance() - amount, self.transactions() + self.__transactions)


class SavingsAccount(Details):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate
        
    def calculate_interest(self):
        interest = round(self.balance() * self.__interest_rate, 2)
        self.__transactions = ["Interest: $" + str(interest)]
        self.setData(self.account_number(), self.balance() + interest, self.transactions() + self.__transactions)


def main():
    checking = CheckingAccount("123456", 1000.00)
    savings = SavingsAccount("654321", 5000.00, 0.02)

    checking.write_check(100.00)
    savings.calculate_interest()

    print(checking.account_number(), checking.balance(), checking.transactions())
    print(savings.account_number(), savings.balance(), savings.transactions())

if __name__ == "__main__":
    main()
