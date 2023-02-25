loop_trigger = 1
sum = 0

while loop_trigger != 0:
    user_input = input("Enter a number: ")
    
    if user_input.isnumeric():
        if user_input == '0':
            loop_trigger = 0
        else:
            if int(user_input) % 2 == 0:
                sum = sum + (int(user_input)*int(user_input))
            else:
                pass    
    else:
        print(f"Error: '" + user_input + "' is not a valid number. Please try again.")

print("The sum of the squares of the even numbers is: " + str(sum))