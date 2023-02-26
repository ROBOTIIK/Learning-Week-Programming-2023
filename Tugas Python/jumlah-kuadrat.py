sum = 0                                                                     # initializing an int variable to be used
while True:
    print("Enter a number: ", end="") 
    num = input()                                                           # query user for int input
    if (num.isdigit()):                                                     # proceed to calculation if user inputs an int
        if (int(num) == 0):                                                 # check whether user wants to conclude the program
            break
        sum += int(num) ** 2 if int(num) % 2 == 0 else 0                    # add num squared value to sum if num is even
    else:
        print(f"Error: '{num}' is not a valid number. Please try again.")   # remind user to input a valid number
print(f"The sum of the squares of the even numbers is {sum}")               # print the sum of squared even numbers