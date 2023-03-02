lst = []
while True:
    try:
        for i in range(0, 100):
            ele = int(input("Enter a number :  "))
            v = str(ele)
            if ele == 0:
                break
            lst.append(ele)
        for i in lst:
            if i % 2 != 0:
                lst.remove(i)
        res = sum(map(lambda i: i * i, lst))
        print('The sum of the squares of the even numbers is: ' + str(res))
        exit(0)
    except ValueError:
        print('Error: ', str(lst), ' is not a valid number. Please try again.')