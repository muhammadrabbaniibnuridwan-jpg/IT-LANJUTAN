# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Ubah semua huruf menjadi lowercase
kalimat = kalimat.lower()

# Pecah menjadi list kata-kata
kata_kata = kalimat.split()

# Buat dictionary histogram
histogram = {}

for kata in kata_kata:
    if kata in histogram:
        histogram[kata] += 1
    else:
        histogram[kata] = 1

# Cetak hasil histogram
print(histogram)