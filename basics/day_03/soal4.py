# soal 4

# SOAL 4 — Ganjil Genap + Nol

# Input angka:

# 0 → nol
# selain itu:
# genap
# ganjil

a = int(input('masukkan angka: '))

if a == 0:
    print('nol')
elif a > 0 :
    print('positif')
elif a < 0:
    print('negatif')
else:
    print('ganjil')