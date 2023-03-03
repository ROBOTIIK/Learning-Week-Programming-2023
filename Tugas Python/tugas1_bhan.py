#Naufal Bhanu Shidqianto 225150307111018

total = 0
while True:
    try:
        num = input("Enter a number (Enter 0 to finish): ")
        num = int(num)
        if num != 0 and num % 2 == 0:
            total += num * num
        if num == 0:
            break
    except ValueError:
        print(f"\'{num}\' bukan merupakan angka. coba lagi.")
    
print(f"Hasil dari penjumlahan adalah: {total}")