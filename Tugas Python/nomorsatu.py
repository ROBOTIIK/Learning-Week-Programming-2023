kuadrat = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "0":
            break
        num = int(num)
        if num % 2 == 0:
            kuadrat += num ** 2
    except ValueError:
        print("Error: '{}' is not a valid number. Please try again.".format(num))

print("The sum of the squares of the even numbers is:", kuadrat)
