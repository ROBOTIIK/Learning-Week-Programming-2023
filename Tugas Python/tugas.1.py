def square(x):
    temp = 0
    for i in x:
        temp = temp+i*i
    return temp

x = 1
angka = []
while(True):
    x = input("Enter a Number: ")
    if(x == "0"):
       break
    if(x.isdigit()):
        if(int(x)%2 == 0):
            angka.append(int(x))
    else:
        print("Error: '",x,"' is not a valid number. Please try again")

print("The sum of the squares of the even numbers is:",square(x))