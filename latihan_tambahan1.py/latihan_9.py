
count = 0
angka = 2

while count < 5:     # loop sampai dapat 5 bilangan prima
    is_prima = True  # flag awal: anggap prima

    # cek apakah 'angka' bisa dibagi bilangan lain selain 1 dan dirinya sendiri
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break   # kalau sudah ada pembagi, tidak perlu cek lagi

    if is_prima:
        print(angka)
        count += 1  # tambah hitungan prima

    angka += 1 