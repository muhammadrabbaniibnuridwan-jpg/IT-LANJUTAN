
kalimat = input(" masukan sebuah kalimat bebas ")

vokal = "aiueoAIUEO"

for huruf in kalimat :
    if huruf in vokal :
        continue

    print(huruf, end="")

print()

