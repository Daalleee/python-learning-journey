# #soal 1
# SOAL 1 — Nilai Huruf (Basic)

# Input nilai:

# ≥ 90 → A
# ≥ 80 → B
# ≥ 70 → C
# < 70 → D

nilai = int(input('masukkan nilai: '))

if nilai >= 90:
    print('A')
elif nilai >= 80:
    print('B')
elif nilai >= 70:
    print('C')
else:
    print('D')