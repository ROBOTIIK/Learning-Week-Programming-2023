#Naufal Bhanu Shidqianto 225150307111018

class Seseorang:
    def __init__(self, nama, nomor_ID):
        self.nama = nama
        self.nomor_ID = nomor_ID

class Siswa(Seseorang):
    def __init__(self, nama, nomor_ID, daftar_matkul):
        Seseorang.__init__(self, nama, nomor_ID)
        self.daftar_matkul = daftar_matkul

class Profesor(Seseorang):
    def __init__(self, nama, nomor_ID, matkul_ajar):
        Seseorang.__init__(self, nama, nomor_ID)
        self.matkul_ajar = matkul_ajar

s = Siswa("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Profesor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.nama, s.nomor_ID, s.daftar_matkul)
print(p.nama, p.nomor_ID, p.matkul_ajar)