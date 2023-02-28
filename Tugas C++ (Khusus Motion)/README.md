# Tugas C++ (Khusus Motion)
**Tugas ini khusus untuk pendaftar divisi Motion Programming. Namun, tidak apa-apa apabila pendaftar Vision juga mau mengerjakan.**


Kerjakanlah tugas-tugas berikut sesuai instruksi.

Selain itu, buatlah sebuah file bernama `.gitignore` yang berisi nama-nama file .exe yang dihasilkan dari tugas ini. Misal program-program untuk tugas ini dicompile menjadi file-file .exe bernama `soal1.exe` dan `soal2.exe`, maka file `.gitignore` akan berisi:
```
soal1.exe
soal2.exe
```
Ini akan membuat git tidak men-track file-file .exe tersebut.

## Instruksi
### Soal 1
Buatlah sebuah program yang berisi fungsi yang bernama `tukar` yang dapat menukar nilai dari dua variabel. Contoh penggunaan:
```c++
int a = 1;
int b = 2;
tukar(a, b);
cout << a << ' ' << b;  // output: 2 1
```
 Gunakan *function overloading* (lihat [slide PPT ini](https://docs.google.com/presentation/d/10zpZlO1YeS_EIv9d4LqcMg3w6w013guF/edit#slide=id.g2111c88126a_0_6)) untuk menangani tipe-tipe data yang berbeda dengan nama fungsi yang sama. Semua fungsi tersebut harus menggunakan parameter reference (lihat [slide PPT ini](https://docs.google.com/presentation/d/10zpZlO1YeS_EIv9d4LqcMg3w6w013guF/edit#slide=id.g1d4ba691e5d_0_169)) (contoh: `void tukar(int& a, int& b)`).

Program harus dapat menangani tipe data:
- int
- char
- double
- bool
- std::string

**JANGAN GUNAKAN `std::swap`**


Untuk mengetes program, terimalah masukan berikut dan hasilkanlah keluaran berikut. Simpanlah `a` sebagai char, lalu gunakan switch case untuk membedakan antara tipe data. **Apabila terdapat error pada switch case terkait "conflicting declaration", coba apit kode di dalam masing-masing case dengan kurung kurawal.**

#### Format Masukan
Baris pertama berisi `n`.

`n` baris berikutnya berisi `a`, `b`, dan `c` dipisahkan spasi.
- `a` menandakan tipe data dari masukan:
    - `i` berarti int
    - `c` berarti char
    - `d` berarti double
    - `b` berarti bool
    - `s` berarti std::string
- `b` dan `c` merupakan nilai bertipe data `a`

#### Batasan Masukan
- 1 ≤ `n` ≤ 10
- Masukan tidak akan terlalu besar.
- String hanya berupa satu kata.

#### Format Keluaran
`n` baris berisi `c` dan `b` dipisahkan spasi.

#### Contoh Masukan
```console
5
i 10 8
c a b
d 2.0 8.5
b 0 1
s halo dunia
```

#### Contoh Keluaran
```console
8 10
b a
8.5 2.0
1 0
dunia halo
```

----------

### Soal 2
Sebuah robot berada dalam suatu grid koordinat kartesius. Robot tersebut berawal di titik pusat, yaitu koordinat (0, 0).

Buatlah sebuah class Robot yang dapat menerima perintah, lalu bergerak sesuai perintah tersebut. Setiap kali bergerak, robot harus mengatakan arah mata angin mana dia bergerak (lihat contoh keluaran). Pada akhir program, sebutkanlah koordinat akhir robot. Untuk itu, class Robot harus dapat menyimpan koordinat dimana dia berada.

Pisahkanlah program menjadi tiga file (lihat [slide PPT ini](https://docs.google.com/presentation/d/10zpZlO1YeS_EIv9d4LqcMg3w6w013guF/edit#slide=id.g1d4ba691e5d_0_388) untuk contoh):
- Robot.h
- Robot.cpp
- main.cpp

Opsional: ketiga file boleh dikelompokkan ke dalam satu folder sendiri.

Untuk mengcompilenya, lihat [slide PPT ini](https://docs.google.com/presentation/d/10zpZlO1YeS_EIv9d4LqcMg3w6w013guF/edit#slide=id.g1d4ba691e5d_0_430).


#### Format Masukan
Baris pertama berisi `n`, yaitu jumlah perintah.

`n` baris berikutnya berisi `x` dan `y` dipisahkan spasi yang menandakan robot bergerak sejauh `x` di sumbu X dan sejauh `y` di sumbu Y.

#### Batasan Masukan
- 1 ≤ `n` ≤ 10
- -100 ≤ `x`, `y`, ≤ 100
- `x` dan `y` tidak akan pernah dua-duanya 0.

#### Format Keluaran
`n` baris berisi arah mata angin kemana robot bergerak, diikuti dengan satu baris yang mengatakan koordinat akhir robot.

#### Contoh Masukan
```console
6
5 0
-3 0
0 2
0 -6
1 1
-10 1
```

#### Contoh Keluaran
```console
TIMUR
BARAT
UTARA
SELATAN
TIMUR LAUT
BARAT LAUT
KOORDINAT AKHIR: (-7, -2)
```