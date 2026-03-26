# soal 9

# Kategori BMI (Logika gabungan)

# Input berat & tinggi:
# Hitung BMI = berat / (tinggi * tinggi)

# Kategori:

# < 18.5 → kurus
# 18.5–24.9 → normal
# 25–29.9 → gemuk
# ≥ 30 → obesitas

berat = float(input('masukkan berat: '))
tinggi = float(input('masukkan tinggi: '))

BMI = berat / (tinggi * tinggi)

if BMI >= 30:
    print('obesitas')
elif BMI >=25:
    print('gemuk')
elif BMI >= 18.5:
    print('normal')
else:
    print('kurus')
