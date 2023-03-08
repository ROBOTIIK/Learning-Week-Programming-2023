k=1
total=int(0)

while not k==0 :
    print("Enter a number:", end=' ')
    k = input()
    if (k.isnumeric()):
        k = int(k)
        
        if (k==0):
            print("The sum of the squares of the even numbers is: ", total)
            break
        
        else:
            if(k%2==0):
                total += k**2
            
    else:
        print("Error: '"+ k +"' is not a valid number. Please try again.")