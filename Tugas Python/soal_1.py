final_sum = 0
while True:
    user_input = input("Enter a number : ")
    validation = user_input.isdigit()
    if validation == True:
        sum = int(user_input) ** 2
        final_sum += sum
        if int(user_input) == 0:
            print("The sum of the squares of the even number is : ", final_sum)
            break
    else:
        print("Error : ", user_input, "is not a valid number. Please try again")