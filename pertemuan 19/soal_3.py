teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

import re
# Pakai re.search
hasil_search = re.search("python", teks)
if hasil_search:
    print("Hasil re.search:", hasil_search.group())

# Pakai re.findall
hasil_findall = re.findall("python", teks)
print("Hasil re.findall:", hasil_findall)

# re.search('python', teks)
#  mencari kemunculan pertama dari pola "python" di string.
#  Mengembalikan objek match (bukan langsung string).
#  Kalau mau ambil teks hasil temuan, gunakan .group().
#  Di contoh ini, hasilnya "python" (yang pertama ditemukan).

# re.findall('python', teks)
#  mencari semua kemunculan pola "python" di string.
#  Mengembalikan list berisi semua hasil.
#  Di contoh ini, hasilnya ['python', 'python'] karena ada 2 kali kata "python"