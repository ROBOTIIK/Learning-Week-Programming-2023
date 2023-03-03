sum = int (0)
while True:
    angka = input("Enter a number:")
    if angka.isnumeric() :
        angka = int(angka)
        if angka == 0 : 
            break

        elif angka %2 == 0:
            sum += (angka ** 2)
    else:
        print (f"Error: '{angka}' is not a valid number. Please try again.")
print("The sum of the squares of the even numbers is:", sum)
