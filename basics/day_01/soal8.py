#soal 8

#soal 9
x = int(input('masukkan angka: '))
def cek_angka(x):
    if x % 2 == 0:
        return 'genap'
    else:
        return 'ganjil'
print(cek_angka(x))