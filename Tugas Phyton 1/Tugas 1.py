nilai = []
value = 0

while (True):
    try:
        num = int (input("Enter a number: ".format(value)))
        nilai.append(int(num))
        value += 1
        print (nilai)

        if int(value) == 0:
            def square(nilai):
                return [value**2 for value in nilai]
            print (sum(nilai))
            break

    except ValueError:
        print("\nError : ", num, "is not a valid number, please try again")
    
