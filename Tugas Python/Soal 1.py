def kuadrat(x):
    temp = 0
    for i in x:
        temp = temp+i*i
    return temp

ulang = 1
angka = []
while(True):
    ulang = input("Enter a Number: ")
    if(ulang == "0"):
       break
    if(ulang.isdigit()):
        if(int(ulang)%2 == 0):
            angka.append(int(ulang))
    else:
        print("Error: '",ulang,"' is not a valid number. Please try again")

print("The sum of the squares of the even numbers is:",kuadrat(angka))


    
    

