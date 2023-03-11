# Duta Kukuh Pribadi

angka = None

bilTotal = 0

while angka != 0:
    try:
        angka = input("Enter a number : ")
        angka = int(angka)

    except :
        print("Error:\'", angka , "\'is not a valid number. Please try again.")

    else : 
        if angka % 2 == 0:
            bilTotal += angka*angka

print("The sum of the squares of the even numbers is:" , bilTotal)





