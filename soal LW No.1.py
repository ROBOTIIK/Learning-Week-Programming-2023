def BilanganKuadrat (): 
    sum = 0
    angka = 1
    while angka != 0:
        angka = input('Enter a number: ')
        if angka.isnumeric():
            if int(angka) == 0:
                break
            if int(angka) % 2 == 0:
                sum += (int(angka) ** 2)
        else :
            print("Error: ", "'",angka, "'", "is not a valid number, Please try again")
    print("The sum of the squares of the even number is : ", sum)

BilanganKuadrat ()
