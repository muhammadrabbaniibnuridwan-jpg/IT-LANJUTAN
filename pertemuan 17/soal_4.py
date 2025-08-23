# Dictionary papan catur dengan tuple sebagai key
papan_catur = {}

# Isi beberapa posisi
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(8, 'g')] = "Kuda Hitam"

# Akses bidak di posisi (1, 'a')
print("Isi posisi (1, 'a'):", papan_catur[(1, 'a')])

#Key dictionary berupa tuple (baris, kolom) → contoh (1, 'a').

#Value dictionary adalah nama bidak (string).

#Akses biasa dengan papan_catur[(1, 'a')].