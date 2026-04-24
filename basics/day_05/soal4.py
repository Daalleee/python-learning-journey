# soal 4

# Umur + Kategori

# Input umur:

# jika ≥ 18 → dewasa
# jika ≥ 60 → lansia
# jika < 18 → belum dewasa

umur = int(input('masukkan umur: '))

if umur >= 18:
    if umur >= 60:
        print('lansia')
    else:
        print('dewasa')
else:
    print('belum dewasa')