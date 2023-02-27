
matkul_belajar = []
matkul_ajar = []

class Person:
    def __init__(self, nama, id_num):
        self.nama = nama
        self.id_num = id_num

class Student(Person):
    def __init__(self, nama, id_num, matkul_belajar):
        Person.__init__(self, nama, id_num)
        self.matkul_belajar = matkul_belajar

    def nama(self):
        print(self.nama)
    def id_num(self):
        print(self.id_num)
    def matkul_belajar(self):
        print(self.matkul_belajar)

class Professor(Person):
    def __init__(self, nama, id_num, matkul_ajar):
        Person.__init__(self, nama, id_num)
        self.matkul_ajar = matkul_ajar
        
    def nama(self):
        print(self.nama)
    def id_num(self):
        print(self.id_num)
    def matkul_ajar(self):
        print(self.matkul_ajar)

s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.nama, s.id_num, s.matkul_belajar)
print(p.nama, p.id_num, p.matkul_ajar)