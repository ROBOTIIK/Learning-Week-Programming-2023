## Fawwaz Anrico Purnomo 215150301111019
num = None
total = 0
while num != 0:
    try:
        num = input('Enter a number : ')
        num = int(num)
    except:
        print("Error:\'", num , "\'is not a valid number. Please try again.")
    else:
        if num % 2 == 0 : 
            total+= num*num

print("The sum of the squares of the even numbers is:" , total)