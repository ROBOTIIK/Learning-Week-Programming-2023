sum = 0

while True:
    try:
        number = input("Enter a number: ")
        number = int(number)

        if number == 0:
            break

        elif number % 2 == 0:
            sum += (number * number)
    
    except ValueError:
        print(f"Error: '{number}' is not a valid number. Please try again.")
        

print("The sum of the squares of the even numbers is:", sum)