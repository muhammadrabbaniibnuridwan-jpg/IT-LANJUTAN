class kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("meow")

    def perkenalkan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.") 

   
# Membuat object dari class Kucing
kucing1 = kucing("ah tong", "Oranye")
kucing2 = kucing("getong", "abu abu")

# Memanggil method dari masing-masing objek
kucing1.perkenalkan_diri()
kucing1.bersuara()

kucing2.perkenalkan_diri()
kucing2.bersuara()

