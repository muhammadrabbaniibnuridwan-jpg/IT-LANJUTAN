#jawaban no 4
a = [1, 2, 3, 4, 5]
b = a           # ALIAS (b dan a menunjuk list yang sama)
c = a.copy()    # COPY (list baru)

b[1] = 20       # Ubah indeks ke-1 melalui b
c[1] = 30       # Ubah indeks ke-1 pada c

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
