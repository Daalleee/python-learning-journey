# soal 8

# Nilai + Status

# Input nilai:

# ≥ 75 → lulus
# < 75 → tidak lulus

# Tambahan:

# ≥ 90 → "lulus dengan sangat baik"

n = int(input('masukkan nilai: '))

if n >= 90:
    print('lulus dengan sangat baik')
elif n >= 75:
    print('lulus')
else:
    print('tidak lulus')