# Inisialisasi variabel
total_kuadrat_genap = 0
finish = False

# Meminta input dari pengguna
while not finish:
    try:
        number = input("Enter a number: ")
        number = int(number)
        if number == 0:
            finish = True
        elif number % 2 == 0:
            total_kuadrat_genap += number ** 2
    except ValueError:
        print(f"Error: '{number}' is not a valid number. Please try again.")

# Menampilkan hasil
print("The sum of the squares of the even numbers is:", total_kuadrat_genap)
