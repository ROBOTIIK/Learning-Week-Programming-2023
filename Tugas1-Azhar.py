hasil_jumlah = 0

while True:
   inputan = input("Enter a number : ")
   check = inputan.isdigit()
   if check == True:
      hasil = int(inputan) ** 2
      hasil_jumlah += hasil
      if int(inputan) == 0:
         print ("The sum of the squares of the even number is : ", hasil_jumlah)
         break
   else:
      print ("Error : ", inputan, "is not a valid number. Please try again")