
while True :
    try :
        umur = int(input("masukan nama lu bre: "))

        if umur <= 18 :
            print("masukan umur 18 atau lebih")

        elif umur >= 50 :
            print("maaf umur anda ketuaan ")

        else :
            print( "makasih umur anda sudah dewasa dan gak ketuaan") 
        
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bukan huruf kocak.")