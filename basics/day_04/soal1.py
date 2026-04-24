# soal 4

# Rentang Angka

# Input angka:

# 1–10 → "kecil"
# 11–100 → "sedang"

# 100 → "besar"

angaka = int(input('masukkan angaka: '))

if angaka >= 100:
    print('besar')
elif angaka >= 11:
    print('sedang')
else:
    print('kecil')