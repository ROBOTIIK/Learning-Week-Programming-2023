class Tabungan:
    def __init__(self, no_rek, saldo, bunga, transaksi=None):
        self.no_rek = no_rek
        self.saldo = float(saldo)
        self.bunga = float(bunga)
        self.transaksi = transaksi

    def setor(self, uang):
        self.saldo = self.saldo + float(uang)
        self.transaksi = f"['Deposit: ${float(uang)}, 'Savings: ${self.saldo}']"

    def Withdraw(self, uang):
        self.saldo = self.saldo - float(uang)
        self.transaksi = f"['Withdrawal: ${float(uang)}, 'Savings: ${self.saldo}']"

    def hitung_bunga(self):
        suku = self.saldo * self.bunga
        self.saldo = self.saldo + suku
        self.transaksi = f"['Deposit: ${suku}, 'Interest: ${suku}']"


class Giro:
    def __init__(self, no_rek, saldo, transaksi=None):
        self.no_rek = no_rek
        self.saldo = float(saldo)
        self.transaksi = transaksi

    def setor(self, uang):
        self.saldo = self.saldo + float(uang)
        self.transaksi = f"['Deposit: ${float(uang)}, 'Savings: ${self.saldo}']"

    def Withdraw(self, uang):
        self.saldo = self.saldo - float(uang)
        self.transaksi = f"['Withdrawal: ${float(uang)}, 'Savings: ${self.saldo}']"

    def tulis_cek(self, uang):
        self.saldo = self.saldo - uang
        self.transaksi = f"['Withdrawal: ${uang}, 'Check: ${uang}']"


class Akun_tabungan(Tabungan):
    def __init__(self, no_rek, saldo, bunga):
        Tabungan.__init__(self, no_rek, saldo, bunga)


class Akun_giro(Giro):
    def __init__(self, no_rek, saldo):
        Giro.__init__(self, no_rek, saldo)


a = Akun_giro("123456", "1000.00")
b = Akun_tabungan("654321", "5000.00", "0.02")
a.tulis_cek(100.00)
b.hitung_bunga()
print(a.no_rek, a.saldo, a.transaksi)
print(b.no_rek, b.saldo, b.transaksi)
