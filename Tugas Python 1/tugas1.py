angka = []
i = 0
jumlah = 0

def stop():
    jumlah = 0
    for item in angka:
        jumlah += item**2
    print ("The sum of the squares of the even numbers is: ", jumlah)
  

while (True):
    angka_baru = input("Enter a number: ".format(i))   
    cek = angka_baru.isdigit()
    if cek == True:
        angka.append(int(angka_baru))
        i+=1
        if int(angka_baru) == 0:
            stop()
            break
    else:
        print("Error : ", angka_baru, "is not a valid number, please try again")


    

    

    


        

