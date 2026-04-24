# soal 6

# Diskon Belanja

# Input total belanja:

# ≥ 100000 → diskon 20%
# ≥ 50000 → diskon 10%
# < 50000 → tidak ada diskon

total = int(input('masukkan total belanja: '))

if total >= 100000:
    print('diskon 20%')
elif total >= 50000:
    print('diskon 10%')
else:
    print('tidak ada diskon')