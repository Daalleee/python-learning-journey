# soal 2

# Tiket Umur

# Input umur:

# < 5 → gratis
# 5–17 → bayar 10k
# ≥ 18 → bayar 20k

umur = int(input('masukkan umur: '))

if umur >= 18:
    print('bayar 20k')
elif umur >= 5:
    print('bayar 10k')
else:
    print('gratis')