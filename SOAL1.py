numbers = []
while True:
    try:
        num = input("Enter a number : ")
        rnum = num
        if num == '0':
            break
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("Error: "+rnum+" is not a valid number. Please try again. ")

even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num**2

print("The sum of the squares of the even numbers is: ", even_sum)