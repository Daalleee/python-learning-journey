#soal 3
# SOAL 3 — Nilai Huruf
# input nilai (0–100)
# 90–100 → A
# 80–89 → B
# 70–79 → C
# <70 → D

nilai = int(input('masukkan nilai: '))

if nilai >= 90:
    print('A')
elif nilai >= 80:
    print('B')
elif nilai >= 70:
    print('C')
else:
    print('D')