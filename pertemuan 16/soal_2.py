# 1) Buat dictionary kosong
kontak = {}
print("Awal:", kontak)  # {}

# 2) Tambahkan tiga kontak
# Catatan: nomor telepon disimpan sebagai string agar leading zero tidak hilang.
kontak["Ibu"] = "0812-3456-7890"
kontak["Ayah"] = "0821-2345-6789"
kontak["Teman"] = "0851-9876-5432"
print("Setelah tambah 3 kontak:", kontak)

# 3) Ubah nomor telepon "Ibu"
# Mengubah value untuk key yang sama akan menimpa (overwrite) nilai lama.
kontak["Ibu"] = "0813-1111-2222"
print('Setelah ubah nomor "Ibu":', kontak)

# 4) Hapus "Teman" dengan .pop()
# .pop(key) mengembalikan value yang dihapus; bisa kita simpan/print bila perlu.
dihapus = kontak.pop("Teman")  # jika "Teman" tidak ada, ini akan KeyError
print(f'Menghapus "Teman" (nomor: {dihapus})')
print("Setelah pop Teman:", kontak)

# 5) Cetak dictionary kontak akhir
print("\nKontak akhir:", kontak)