class BankAcc:
    def __init__(self, nomor_rek, saldo):
        self.nomor_rek = nomor_rek
        self.saldo = saldo
        self.transaksi = []

    def setor(self, uang):
        self.saldo += uang 
        self.transaksi.append(f"Deposit: ${uang:.2f}")

    def tarik(self, uang):
        if self.saldo >= uang :
            self.saldo -= uang
            self.transaksi.append(f"Withdrawal: ${uang:.2f}")
        else :
            print("Insufficient balance!")

class RekeningGiro(BankAcc):
    def __init__(self, nomor_rek, saldo):
        super().__init__(nomor_rek, saldo)

    def tulis_cek(self, uang):
        self.tarik(uang)
        self.transaksi.append(f"Check: ${uang:.2f}")

class RekeningTabungan(BankAcc):
    def __init__(self, nomor_rek, saldo, suku_bunga):
        super().__init__(nomor_rek, saldo)
        self.suku_bunga = suku_bunga

    def hitung_bunga(self):
        bunga = self.saldo * self.suku_bunga
        self.setor(bunga)
        self.transaksi.append(f"Interest: ${bunga:.2f}")

checking = RekeningGiro("123456", 1000.00)
savings = RekeningTabungan("654321", 5000.00, 0.02)

checking.tulis_cek(100.00)
savings.hitung_bunga()

print(checking.nomor_rek, checking.saldo, checking.transaksi)
print(savings.nomor_rek, savings.saldo, savings.transaksi)

