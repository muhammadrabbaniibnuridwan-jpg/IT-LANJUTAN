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

