class rekeningbank:
    def __init__(self, nomer_rekening, nama_pemilik):
        self.nomer_rekening = nomer_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def lihat_saldo(self):
        print(f"Saldo saat ini: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}. Saldo baru: Rp{self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("saldo tidak mencukupi")

        else :
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Saldo baru: Rp{self.saldo}")

# Membuat objek rekening_budi
rekening_rabbani = rekeningbank("1234567890", "rabbani") 

# Coba method-methodnya
rekening_rabbani.lihat_saldo()
rekening_rabbani.setor(100000)
rekening_rabbani.setor(50000)
rekening_rabbani.tarik(200000)  # gagal karena saldo tidak cukup
rekening_rabbani.tarik(70000)   # berhasil
rekening_rabbani.lihat_saldo()

