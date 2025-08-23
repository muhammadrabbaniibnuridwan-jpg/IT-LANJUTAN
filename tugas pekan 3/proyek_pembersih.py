# proyek_pembersih.py

def pembersih_data():
    try:
        # Buka file input untuk dibaca
        with open("transaksi_kotor.txt", "r") as file_input:
            # Buka file output untuk ditulis
            with open("laporan_bersih.txt", "w") as file_output:
                
                # Header laporan
                file_output.write("LAPORAN TRANSAKSI BERSIH\n")
                file_output.write("=========================\n\n")

                grand_total = 0  # untuk bonus challenge

                # Loop baris demi baris
                for baris in file_input:
                    # Bersihkan spasi dan newline
                    baris = baris.strip()

                    # Skip baris kosong
                    if not baris:
                        continue
                    
                    # Pecah data dengan koma
                    data_potongan = baris.split(",")

                    # Pastikan data terdiri dari 4 bagian
                    if len(data_potongan) != 4:
                        continue
                    
                    # Bersihkan dan format setiap bagian
                    id_bersih = data_potongan[0].strip().upper()
                    nama_bersih = data_potongan[1].strip().title()
                    jumlah_bersih = int(data_potongan[2].strip())
                    harga_bersih = float(data_potongan[3].strip())

                    # Hitung total harga
                    total_harga = jumlah_bersih * harga_bersih

                    # Filter: hanya tulis jika total > 500k (bonus)
                    # if total_harga <= 500000:
                    #     continue

                    # Akumulasi ke grand_total
                    grand_total += total_harga

                    # Format string output
                    string_output = (
                        f"ID: {id_bersih} | "
                        f"Produk: {nama_bersih} | "
                        f"Jumlah: {jumlah_bersih} | "
                        f"Total Harga: Rp {total_harga}\n"
                    )

                    # Tulis ke file output
                    file_output.write(string_output)

                # Footer
                file_output.write("\n--- ANALISIS SELESAI ---\n")
                file_output.write(f"TOTAL KESELURUHAN: Rp {grand_total}\n")

        print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

    except FileNotFoundError:
        print("Error: bang file gak di temukan ")


# Jalankan fungsi
if __name__ == "__main__":
    pembersih_data()  
