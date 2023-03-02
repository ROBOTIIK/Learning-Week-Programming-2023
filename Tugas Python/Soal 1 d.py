sum = 0
trigger = 1
            
while trigger != 0:
    nomor = input('Enter a number: ')
    if nomor.isnumeric():
        if nomor == '0':
            trigger = 0
        else:
            if int(nomor) % 2 == 0:
                sum += int(nomor)**2
    else:
        print('Error: \''+ nomor +'\' is not a valid number. Please try again.')

print('The sum of the squares of the even number is:',sum)