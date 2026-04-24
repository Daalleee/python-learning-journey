# soal 3

# Lulus + Grade 

# Input nilai:

# ≥ 75 → lulus
# < 75 → tidak lulus

# Tambahan:

# ≥ 90 → "lulus dengan sangat baik"

nilai = float(input('masukkan nilai: '))

if nilai >= 90:
    print('lulus dengan sangat baik')
elif nilai >= 75:
    print('lulus')
else:
    print('tidak lulus')