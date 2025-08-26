for angka in range(20, 0, -1):  # dari 20 sampai 1
    if angka % 4 == 0:
        print(f"{angka} (dilewati)")
        continue
    print(angka)