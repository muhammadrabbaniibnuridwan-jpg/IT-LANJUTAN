
password = "katasandi123"
karakter_terlarang = "$%&"

for karakter in password:
    if karakter in karakter_terlarang:
        print("paswword mengandung karakter terlarang")
        break
else :
    print(" paswword aman")

    