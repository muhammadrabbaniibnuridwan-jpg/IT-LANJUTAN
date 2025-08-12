#jawaban no 1
# Membuat list jadwal Senin
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print("Jadwal hari Senin:", jadwal_senin)

# Cetak mata pelajaran pertama
print("Pelajaran pertama:", jadwal_senin[0])

# Cetak mata pelajaran terakhir dengan indeks negatif
print("Pelajaran terakhir:", jadwal_senin[-1])


# jawabn no 2 

# Ubah "Olahraga" menjadi "Kimia"
jadwal_senin[2] = "Kimia"
# Cetak hasil pembaruan
print("Jadwal Senin setelah diperbarui:", jadwal_senin)

#Penjelasan:
#List bersifat mutable, jadi jadwal_senin[2] bisa langsung diubah.


#jawaban no 3

nilai_mentah = [55, 63, 72, 81, 90]

# Tambahkan nilai bonus 5 ke setiap elemen
for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5

# Cetak hasil
print("Nilai setelah ditambah bonus:", nilai_mentah)


#Penjelasan:
#range(len(nilai_mentah)) → menghasilkan indeks 0 sampai 4.
#nilai_mentah[i] += 5 → menambah 5 poin ke setiap nilai.

awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Gabungkan list
seminggu = awal_minggu + akhir_minggu

# Ambil hari kerja (Senin sampai Jumat)
hari_kerja = seminggu[0:5]

# Cetak hasil
print("Hari kerja:", hari_kerja)


#Penjelasan:
#awal_minggu + akhir_minggu → membuat list baru seminggu.
#seminggu[:5] → slicing dari indeks 0 sampai sebelum 5 (Senin–Jumat).


















# # List berisi integer
# nilai_ujian = [90, 80, 70, 60]

# # List berisi string
# nama_hewan = ["Kucing", "Anjing", "Burung", "Ikan"]

# # List berisi tipe data campuran
# data_mahasiswa = ["Andi Pratama", 21, 85.5, True]

# # List kosong
# daftar_belanja = []

# # Nested list (list di dalam list)
# matriks = [
#     ["Kucing", "Anjing", "Burung", "Ikan"],
#     ["Andi Pratama", 21, 85.5, True]
# ]

# print(type(nama_hewan)) 

# angka = [10, 20, 30, 40, 50]
# angka[2] = 35      # ubah elemen indeks 2
# angka[-1] = 99     # ubah elemen terakhir
# print(angka) 

# buah = ["Apel", "Jeruk", "Mangga", "Durian", "Semangka"]

# print(buah[0])   # Apel (indeks pertama)
# print(buah[2])   # Mangga (indeks ketiga)
# print(buah[-1])

# daftar_kota = ["Jakarta", "Bandung", "Surabaya", "Medan"]
# for kota in daftar_kota:
#     print(kota)

# angka = [10, 20, 30, 40, 50]
# for i in range(len(angka)):
#     angka[i] *= 2
# print(angka) 