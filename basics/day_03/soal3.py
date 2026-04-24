# soal 3

# SOAL 3 — Bilangan

# Input angka:

# 0 → positif

# < 0 → negatif
# = 0 → nol

angka = int(input('masukkan angka: '))

if angka == 0:
    print('nol')
elif angka > 0:
    print('positif')
else:
    print('negatif')