# soal 10

# Penilaian Lengkap 🔥🔥

# Input:

# nilai tugas
# nilai ujian

# Aturan:

# tugas ≥ 70 dan ujian ≥ 70 → lulus
# salah satu < 70 → tidak lulus

# Tambahan:
# jika dua-duanya ≥ 90 → "lulus dengan predikat A"

tugas = float(input('masukan nilai tugas: '))
ujian = float(input('masukkan nilai ujian: '))

if tugas >= 90 and ujian >= 90:
    print('lulus dengan predikat A')
elif tugas >= 70 and ujian >= 70:
    print('lulus')
elif tugas >= 70 and not ujian >= 70:
    print('tidak lulus')
else:
    print('tidak lulus')