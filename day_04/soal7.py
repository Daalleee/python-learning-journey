# soal 7

# Nilai Validasi

# Input nilai:

# jika < 0 atau > 100 → "nilai tidak valid"
# selain itu:
# ≥ 75 → lulus
# < 75 → tidak lulus

nilai = int(input('masukkan nilai: '))

if nilai > 100 :
    print('nilai tidak valid')
elif nilai <= 0:
    print('nilai tidak valid')
elif nilai >= 75:
    print('lulus')
else:
    print('tidak lulus')