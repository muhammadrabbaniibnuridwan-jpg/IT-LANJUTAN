# Nested dictionary untuk 2 produk
produk = {
    "PROD001": {
        "nama": "Laptop",
        "harga": 8500000,
        "stok": 5
    },
    "PROD002": {
        "nama": "Headphone",
        "harga": 250000,
        "stok": 15
    }
}

# Cetak nama dan harga produk dengan ID PROD002
print("Nama Produk:", produk["PROD002"]["nama"])
print("Harga:", produk["PROD002"]["harga"])