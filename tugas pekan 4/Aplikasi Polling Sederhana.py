# proyek_polling.py

# Struktur data survei
SURVEI = [
    {
        "pertanyaan": "Apa agama mu?",
        "opsi": ["kristen", "islam", "hindu", "budda"]
    },
    {
        "pertanyaan": "apa nama kitab suci mu?",
        "opsi": ["quran", "injil", "taurot"]
    },
    {
        "pertanyaan": "cita cita kmu mau menjadi?",
        "opsi": ["pemain bola", "dokter", "guz", "kyai","pak ustadz"]
    }
]

# Inisialisasi hasil polling
hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

print("="*44)
print("     SELAMAT DATANG DI APLIKASI POLLING")
print("="*44)

# Loop utama untuk setiap pertanyaan
for idx, item_survei in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {idx}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]:
        print(f"  - {opsi}")

    # Validasi input
    while True:
        jawaban = input("Jawaban Anda: ").strip()
        if jawaban in item_survei["opsi"]:
            hasil_polling[jawaban] += 1
            print(f"> {jawaban} --- Terima kasih! ---")
            break
        else:
            print(f"> {jawaban}\nJawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# Tampilkan hasil polling
print("="*44)
print("             HASIL POLLING")
print("="*44)

total_suara = sum(hasil_polling.values())
for opsi, jumlah in hasil_polling.items():
    persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
    print(f"{opsi} : {jumlah} suara ({persentase:.2f}%)")

print("="*44)

# BONUS: Simpan hasil polling ke file
with open("hasil_polling.txt", "w", encoding="utf-8") as f:
    f.write("HASIL POLLING\n")
    f.write("="*30 + "\n")
    for opsi, jumlah in hasil_polling.items():
        persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
        f.write(f"{opsi} : {jumlah} suara ({persentase:.2f}%)\n")