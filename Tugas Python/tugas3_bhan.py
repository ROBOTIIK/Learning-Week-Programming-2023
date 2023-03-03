#Naufal Bhanu Shidqianto 225150307111018

class Akun:
    def __init__(self, no_rekening, saldo):
        self.no_rekening = no_rekening
        self.saldo = saldo
        self.transaksi = []
        
    def penarikan(self, jumlah):
        self.transaksi = [f'Withdrawal = ${jumlah}']
        self.saldo -= jumlah

    def setoran(self, jumlah):
        self.transaksi = [f'Deposit = ${jumlah}']
        self.saldo += jumlah
   
class rekening_giro(Akun):
    def __init__(self, no_rekening, saldo):
        Akun.__init__(self, no_rekening, saldo)
    
    def menulis_cek(self, jumlah):
        self.jumlah = jumlah
        self.saldo -= jumlah
        self.transaksi = [f'Withdrawal: ${jumlah}', f'Check: ${jumlah}']
        
class rekening_tabungan(Akun):
    def __init__(self, no_rekening, saldo, suku_bunga):
        Akun.__init__(self, no_rekening, saldo)
        self.suku_bunga = suku_bunga
    
    def menghitung_bunga(self):
        self.rumus_sukubunga = 0
        self.rumus_sukubunga = self.saldo*self.suku_bunga
        self.saldo += self.saldo*self.suku_bunga
        self.transaksi = [f'Deposit: ${self.rumus_sukubunga}', f'Interest: ${self.rumus_sukubunga}']

giro = rekening_giro("123456", 1000.00)
tabungan = rekening_tabungan("654321", 5000.00, 0.02)

giro.menulis_cek(100.00)
tabungan.menghitung_bunga()

print(giro.no_rekening, giro.saldo, giro.transaksi)
print(tabungan.no_rekening, tabungan.saldo, tabungan.transaksi)