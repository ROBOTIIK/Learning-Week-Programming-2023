angka = []
hasil = 0
while True:
    angkaku = input("Masukkan Angka :")
    if angkaku == '0':
        break
    try:
        int(angkaku)
        angka.append(int(angkaku))
    except ValueError:
        print("Error: '" + angkaku + "' Bukanlah sebuah angka")

for x in angka:
    hasil = int(hasil) + pow(x, 2)
    
print(f'Jumlan dari pengkuadratan beberapa angka adalah : {hasil}')
    

