# soal1

def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Error: Input must be a valid number. Please try again.")

sum_of_squares = 0
while True:
    num = get_valid_number()
    if num == 0:
        break
    elif num % 2 == 0:
        sum_of_squares += num ** 2

print(f"The sum of the squares of the even numbers is: {sum_of_squares}")