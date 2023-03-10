total = 0
while True:
    user_input = input("Enter a number : ")
    ver = user_input.isdigit()
    if ver == True:
        sum = int(user_input) ** 2
        total += sum
        if int(user_input) == 0:
            print("The sum of the squares of the even number is : ", total)
            break
    else:
        print("Error : ", user_input, "is not a valid number. Please try again")
