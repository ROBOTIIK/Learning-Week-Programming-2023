#-----Membuat wadah berupa List kosong----------
wadahAngka = []
#-----Inisialisasi wadah hasil------------------
hasil = 0

#-----Looping untuk masukkan dari user----------
while True :
    try :
        inputan = input('Enter a number: ')
        angka2 = int(inputan)
        if angka2 == 0:
            break
        else:
            wadahAngka.append(angka2)

    except ValueError:
         print('Error: "{error}" is not a valid number. Please try again'.format(error=inputan))


#-----Proses perhitungan berdasarkan angka yang sudah dimasukkan kedalam list-----------
for angka2 in wadahAngka:
    if angka2 % 2 == 0:
            hasil += angka2**2

            
#-----Proses pencetakan hasil-------------------------------------------------------
print('The sum of the squares of the even numbers is: {hasil}'.format(hasil=hasil))

