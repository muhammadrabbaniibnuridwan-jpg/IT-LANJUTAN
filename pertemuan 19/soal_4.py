# \w+ → satu atau lebih huruf/angka/underscore (mewakili kata)

# g → harus diakhiri huruf g

# \b → word boundary (batas kata, misalnya spasi, koma, titik)
import re

kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."

kata_g = re.findall(r'\w+g\b', kalimat)
print(kata_g)