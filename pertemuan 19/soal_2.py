import re

# minta input dari pengguna
nomor = input("Masukkan nomor telepon: ")

# cek apakah semua digit (regex) dan panjangnya 10-13
if re.search(r'^\d+$', nomor) and 10 <= len(nomor) <= 13:
    print("Format nomor telepon valid.")
else:
    print("Format tidak valid.")