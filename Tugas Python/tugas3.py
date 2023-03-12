class tabungan:
    def __init__(self, rek, saldo, bunga, transaksi=None):
        self.rek = rek
        self.saldo = float(saldo)
        self.bunga = float(bunga)
        self.transaksi = transaksi
    def setor(self, uang):
        self.saldo = self.saldo + float(uang)
        self.transaksi = f"['Deposit: ${float(uang)}, 'Savings: ${self.saldo}']"
    def ambil(self, uang):
        self.saldo = self.saldo - float(uang)
        self.transaksi = f"['Withdrawal: ${float(uang)}, 'Savings: ${self.saldo}']"
    def hitung_bunga(self):
        suku = self.saldo*self.bunga
        self.saldo = self.saldo + suku
        self.transaksi = f"['Deposit: ${suku}, 'Interest: ${suku}']"

class giro:
    def __init__(self, rek, saldo,transaksi=None):
        self.rek = rek
        self.saldo = float(saldo)
        self.transaksi = transaksi
    def setor(self, uang):
        self.saldo = self.saldo + float(uang)
        self.transaksi = f"['Deposit: ${float(uang)}, 'Savings: ${self.saldo}']"
    def ambil(self, uang):
        self.saldo = self.saldo - float(uang)
        self.transaksi = f"['Withdrawal: ${float(uang)}, 'Savings: ${self.saldo}']"
    def tulis_cek(self, uang):
        self.saldo = self.saldo - uang
        self.transaksi = f"['Withdrawal: ${uang}, 'Check: ${uang}']"

class akun_tabungan(tabungan):
    def __init__(self, rek, saldo, bunga):
        tabungan.__init__(self, rek, saldo, bunga)

class akun_giro(giro):
    def __init__(self, rek, saldo):
        giro.__init__(self, rek, saldo)

a = akun_giro("123456", "1000.00")
b = akun_tabungan("654321", "5000.00", "0.02")
a.tulis_cek(100.00)
b.hitung_bunga()
print(a.rek, a.saldo, a.transaksi)
print(b.rek, b.saldo, b.transaksi)
    

        