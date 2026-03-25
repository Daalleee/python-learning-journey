#soal 6
# SOAL 6 — Ganjil / Genap + Positif
# input angka
# tampilkan:
# positif/negatif
# ganjil/genap

angka = int(input('masukkan angka: '))

if angka % 2 == 0 :
    print('genap')
else:
    print('ganjil')

if angka < 0:
    print('negatif')
else:
    print('positif')
