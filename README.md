# Learning-Week-Programming-2023
Repository ini akan digunakan sebagai tempat pengumpulan tugas selama proses Learning Week 2023 divisi Programming.

**Bagi yang belum, silakan mengisi [Gform ini](https://forms.gle/iJdF3xTUtCQek65b9) agar dapat mengedit langsung repository ini. Jangan lakukan fork/pull request. Setelah mengisi formnya, tunggu email invitation untuk menjadi colaborator di repo ini**

**Sangat direkomendasikan untuk membaca [PPT Materi mengenai Git ini](https://docs.google.com/presentation/d/1Wp8kBTa2sq6Y2aOkkLFiAM60qpM_g5Qq/edit?usp=sharing&ouid=113951833262011292171&rtpof=true&sd=true) terlebih dahulu, terutama bagi yang tidak hadir pada pertemuan learning week pertama yang membahas materi ini.**


## Tugas Pertama
**WAJIB MENGERJAKAN TUGAS INI TERLEBIH DAHULU**

1. Clone repo ini dengan cara:
    1. Di terminal, masuk ke direktori yang kalian inginkan untuk menyimpan repo ini.
    2. Jalankan `git clone https://github.com/ROBOTIIK/Learning-Week-Programming-2023.git`
    3. Di terminal, masuk ke direktori Learning-Week-Programming-2023
2. Buatlah branch baru dengan nama branch `[Divisi Programming Pilihan]-[Nama Panggilan]`:
    1. contoh: `git branch Motion-Nathan` untuk membuat cabang baru.
    2. contoh: `git checkout Motion-Nathan` untuk pindah ke cabang itu
3. Edit README.md ini di branch kalian menjadi:
```
# [Nama Lengkap] - [NIM]
## Perkenalan
Halo, saya [Nama Panggilan] dari [prodi][tahun angkatan].
## Divisi
Saya mendaftar di divisi:
- [divisi pilihan 1]
- [divisi pilihan 2]
```
4. Commit. Kalau tidak tahu cara melakukan ini, silakan lihat di PPT.
5. Push ke github dengan `git push`
6. Jangan hapus folder repo ini dari laptop kalian karena akan digunakan terus selama learning week.

## Tugas-Tugas Lainnya
Untuk tugas-tugas berikutnya, nanti akan muncul folder baru untuk pengerjaan tugas itu di cabang main. Lakukanlah langkah-langkah berikut:
1. Jalankan perintah `git fetch`
2. Ketika berada di branch kalian, lakukan `git merge origin/main`. Itu akan memunculkan folder tugas itu ke branch kalian, tetapi akan menyebabkan conflict dengan README.md yang utama. Buka file README.md-nya, lalu hapus saja isi README.md yang dari cabang main.
3. Kerjakan tugas sesuai perintah dalam folder itu di branch kalian
4. Commit apabila tugas sudah selesai
5. Lakukan `git push` untuk menyimpan hasil kerja kalian di github
