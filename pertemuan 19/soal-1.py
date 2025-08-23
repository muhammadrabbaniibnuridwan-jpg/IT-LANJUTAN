import re

teks_data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000." 
# Menemukan semua urutan angka 
semua_angka = re.findall(r'\d+', teks_data) 
# Tanda '+' berarti 'satu atau lebih'. Akan kita bahas nanti. 
print(f"Semua angka yang ditemukan: {semua_angka}")

