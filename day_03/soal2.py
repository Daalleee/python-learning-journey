# #soal 2
# SOAL 2 — Kategori Umur

# Input umur:

# < 12 → anak-anak
# 12–17 → remaja
# ≥ 18 → dewasa

umur = int(input('masukkan umur: '))

if umur < 12:
    print('anak-anak')
elif umur >= 12 and umur <= 17:
    print('remaja')
else:
    print('dewasa')