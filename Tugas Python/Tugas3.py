#------------Class Account-----------------------------------
class account:
    def __init__(self, no_rek, saldo):
        self.no_rek = no_rek
        self.saldo = saldo
#--------Fungsi menabung (Account)---------------------------        
    def tabung(self, nominal):
        self.saldo += nominal
        
#--------Fungsi menarik saldo (Account)----------------------
    def tarik(self, nominal):
        if self.saldo >= nominal :
            saldo -= nominal
        else :
            print("Saldo anda tidak mencukupi")

#-----------Class rekening giro-------------------------------
class rekening_giro(account):
    def __init__(self, no_rek, saldo):
        super().__init__(no_rek, saldo)
        self.riwayatTransaksi = []

#----------Fungsi menabung (Rekening Giro)---------------------
    def Deposit(self, nominal):
        super().tabung(nominal)
        self.riwayatTransaksi.append(('Deposit', nominal))

#--------Fungsi Menarik saldo (Rekening Giro)------------------          
    def Withdraw(self, nominal):
        super().tarik( nominal)
        self.riwayatTransaksi.append(('Withdraw', nominal))

#--------Fungsi tulis cek (Rekening Giro)----------------------
    def tulisCek(self, nominal):
        if self.saldo >= nominal:
            self.saldo -= nominal
            self.riwayatTransaksi.append(('Write_check', nominal))
            self.riwayatTransaksi.append(('Withdrawal', nominal))
        else :
            print("Saldo anda tidak mencukupi")

#---------------Class rekening tabungan------------------------
class rekening_tabungan(account):
    def __init__(self, no_rek, saldo,  suku_Bunga):
        super().__init__(no_rek, saldo)
        self.suku_Bunga = suku_Bunga
        self.transaksi = []
#-------Fungsi menabung (Rekening Tabungan)--------------------- 
    def deposit(self, nominal):
        super().tabung(nominal)
        self.transaksi.append(('Deposit', nominal))
#-------Fungsi menarik saldo (Rekening Tabungan)----------------
    def withdraw(self, nominal):
        if self.saldo >= nominal :
            super().tarik(nominal)
            self.transaksi.append(('Deposit', nominal))
        else:
            print("Saldo anda tidak mencukupi")
#----------- Fungsi menghitung suku bunga-----------------------
    def sukuBunga(self):
        suku_bunga = self.saldo*self.suku_Bunga
        self.saldo += suku_bunga
        self.transaksi.append(('Deposit', suku_bunga))
        self.transaksi.append(('Interest', suku_bunga))

#---------Test cases---------------------------------------------
checking = rekening_giro("123456", 1000.00)
savings = rekening_tabungan ("654321", 5000.00, 0.02)

checking.tulisCek(100.00)
savings.sukuBunga()

print(checking.no_rek, checking.saldo, checking.riwayatTransaksi)
print(savings.no_rek, savings.saldo, savings.transaksi)