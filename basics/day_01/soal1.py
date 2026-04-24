
#soal 1
import random
angka = random.randint(1,100)

while True:
    tebak= int(input('masukkan angka(1-100): '))

    if tebak < angka:
        print('terlalu kecil')
    elif tebak > angka:
        print('terlalu besar')
    else:
        print('benar')
        break