sum = 0
n = 1

while n != 0:
    n = input('Enter a number: ')
    if n.isnumeric():

        if int(n) == 0:
            break
        
        elif int(n) % 2 == 0:
            sum += (int(n) * int(n))

    else :
        print("Error: ", n, "is not a valid number, Please try again")
    
print("The sum of the squares of the even number is : ", sum)