class bank_indo:
    def __init__(self, rekening, saldo):
        self.rekening = rekening
        self.saldo = saldo
        self.transaksi = []
        
class giro:
    def __init__(self, rekening, saldo):
        bank_indo.__init__(self, rekening, saldo)
        
    def Check(self, tarik):
        self.tarik = tarik
        self.saldo = self.saldo - self.tarik
        self.transaksi.append(f'Tarik Tunai: ${tarik}') 
        self.transaksi.append(f'Cek: ${tarik}')
        
class tabungan:
    def __init__(self, rekening, saldo, bunga):
        bank_indo.__init__(self, rekening, saldo)
        self.bunga = bunga
    
    def itung_bunga(self):
        bonus = self.bunga * self.saldo
        self.bonus = bonus
        self.saldo = self.saldo + bonus
        self.transaksi.append(f'Setor: ${bonus}')
        self.transaksi.append(f'Bunga: ${bonus}')

giro = giro("123456", 1000.00)
tabungan = tabungan("654321", 5000.00, 0.02)

giro.Check(100.00)
tabungan.itung_bunga()

print(giro.rekening, giro.saldo, giro.transaksi)
print(tabungan.rekening, tabungan.saldo, tabungan.transaksi)
