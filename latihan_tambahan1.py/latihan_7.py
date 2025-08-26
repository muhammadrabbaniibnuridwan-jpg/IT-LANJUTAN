

# Minta input dari pengguna
N = int(input("Masukkan sebuah angka N: "))

i = 1
total = 0  

# Loop while
while i <= N:
    total += i ** 2   
    i += 1            

# Cetak hasil
print(f"Jumlah kuadrat dari {N} bilangan pertama adalah: {total}")



