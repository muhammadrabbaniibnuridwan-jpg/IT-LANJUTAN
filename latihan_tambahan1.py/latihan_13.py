# Minta input dari pengguna
kata = input("Masukkan sebuah kata: ")

# Loop dari 0 sampai panjang kata-1
for i in range(len(kata)):
    potongan = kata[:i+1]   # ambil huruf dari awal sampai ke-i
    print(potongan)