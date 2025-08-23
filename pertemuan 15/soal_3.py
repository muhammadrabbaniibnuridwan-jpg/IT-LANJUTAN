biodata = {
    "nama": "Muhammad Rabbani",
    "umur": 25,
    "hobi": ["Membaca", "Menulis", "Coding"],
    "sudah_menikah": False
}

# Tambahkan key "kota"
biodata["kota"] = "Jakarta"

# Ubah umur menjadi umur tahun depan
biodata["umur"] = biodata["umur"] + 1

print(biodata)


# Tambahkan key "kota"
biodata["kota"] = "Jakarta"

# Ubah umur menjadi umur tahun depan
biodata["umur"] = biodata["umur"] + 1

# Cetak dictionary yang sudah diperbarui
print(biodata)



# Mengakses key "pekerjaan" menggunakan bracket notation (akan error jika tidak ada)
# print(biodata["pekerjaan"])  # <- baris ini akan menyebabkan KeyError

# Menggunakan .get()
print(biodata.get("pekerjaan"))  # Output: None

# Menggunakan .get() dengan nilai default
print(biodata.get("pekerjaan", "Pelajar"))  # Output: Pelajar