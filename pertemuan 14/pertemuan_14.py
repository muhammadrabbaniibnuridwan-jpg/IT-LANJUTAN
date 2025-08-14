#jawbaban no 1

# List kosong
belanjaan = []

# Menambahkan item dengan append
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

# Menambahkan 'Apel' di posisi awal (indeks 0)
belanjaan.insert(0, "Apel")

# Menghapus 'Susu'
belanjaan.remove("Susu")

# Cetak hasil akhir
print("Daftar belanja akhir:", belanjaan)


#jawaban no 2
nilai = [98, 76, 88, 100, 54]

# Mengurutkan tapi tidak mengubah list asli
nilai_terurut = sorted(nilai)

# Cetak
print("List asli:", nilai)
print("List terurut:", nilai_terurut)


#jawaban no 3

# Minta input dari user
kalimat = input("Masukkan sebuah kalimat: ")

# Ubah ke list kata
kata_list = kalimat.split()

# Hitung jumlah kata
jumlah_kata = len(kata_list)
print("Jumlah kata:", jumlah_kata)

# Urutkan berdasarkan abjad
kata_list.sort()
print("Kata-kata terurut:", kata_list)

#jawaban no 4
a = [1, 2, 3, 4, 5]
b = a           # ALIAS (b dan a menunjuk list yang sama)
c = a.copy()    # COPY (list baru)

b[1] = 20       # Ubah indeks ke-1 melalui b
c[1] = 30       # Ubah indeks ke-1 pada c

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
