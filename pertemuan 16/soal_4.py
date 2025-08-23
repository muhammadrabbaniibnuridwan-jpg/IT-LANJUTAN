# Buat dictionary kosong untuk menyimpan frekuensi hari
hari_freq = {}

# Buka file mbox-short.txt
with open("mbox-short.txt", "r") as f:
    for line in f:
        # Cari baris yang dimulai dengan "From "
        if line.startswith("From "):
            kata = line.split()
            hari = kata[2]   # kata ke-3 adalah hari (index 2)
            # Tambahkan ke histogram
            hari_freq[hari] = hari_freq.get(hari, 0) + 1

# Cetak dictionary hasil
print(hari_freq)