# Tugas Python
Buatlah file python untuk masing-masing soal berikut (jadi total 3 file) dan kerjakanlah tugasnya sesuai instruksi.

## Instruksi
### Soal 1
Buatlah program Python yang mengambil daftar angka dari pengguna dan menampilkan jumlah kuadrat dari angka genap dalam daftar. Namun, program juga harus mengeluarkan pesan kesalahan dan meminta pengguna untuk mencoba lagi jika mereka memasukkan nilai non-numerik. Untuk menghentikan program meminta input bisa diberi input "0".

#### Input dan Output
```console
Enter a number: abc
Error: 'abc' is not a valid number. Please try again.
Enter a number: 5
Enter a number: 10
Enter a number: 2
Enter a number: 0
The sum of the squares of the even numbers is: 104
```

```console
Enter a number: 8
Enter a number: hello
Error: 'hello' is not a valid number. Please try again.
Enter a number: 6
Enter a number: 0
The sum of the squares of the even numbers is: 100
```

----------

### Soal 2
Buat hierarki kelas untuk sistem universitas. Sistem harus memiliki kelas dasar untuk seseorang, dengan kelas turunan untuk siswa dan profesor. Kelas siswa harus memiliki variabel instan untuk nama, nomor ID, dan daftar mata kuliah. Kelas profesor harus memiliki variabel instan untuk nama, nomor ID, dan daftar mata kuliah yang diajarkan. Hierarki kelas harus dibuat sehingga kode berikut dapat berjalan dan menghasilkan output berikut.

#### Kode
```python
s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)
```
#### Output
```console
Alice 1234 ['Introduction to Computer Science', 'Data Structures']
Bob 5678 ['Database Systems', 'Web Development']
```

----------

### Soal 3
Buat hierarki kelas untuk sistem perbankan. Sistem harus memiliki kelas dasar untuk akun, dengan kelas turunan untuk rekening giro dan rekening tabungan. Kelas rekening giro harus memiliki variabel instan untuk nomor rekening, saldo, dan riwayat transaksi. Kelas rekening tabungan harus memiliki variabel instan untuk nomor rekening, saldo, dan suku bunga. Kelas rekening giro dan tabungan harus memiliki metode untuk menarik dan menyetor uang, dan kelas rekening giro juga harus memiliki metode untuk menulis cek. Hierarki kelas harus dibuat sehingga kode berikut dapat berjalan dan menghasilkan output berikut.

#### Kode
```python
checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)
```

#### Output
```console
123456 900.0 ['Withdrawal: $100.00', 'Check: $100.00']
654321 5100.0 ['Deposit: $100.00', 'Interest: $100.00']
```