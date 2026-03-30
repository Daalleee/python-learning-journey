# soal 2

# Nilai + Grade 

# Input nilai:

# jika ≥ 75 → lulus
# jika ≥ 90 → "lulus sangat baik"
# selain itu → "lulus"
# jika < 75 → tidak lulus

nilai = float(input('masukkan nilai: '))

if nilai >= 75:
    if nilai >= 90:
        print('lulus sangat baik')
    else:
        print('lulus')
else:
    print('tidak lulus')