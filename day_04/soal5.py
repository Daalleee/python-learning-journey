# soal 5

# Diskon Member

# Input:

# total belanja
# status member (ya/tidak)

# Aturan:

# member & belanja ≥ 100000 → diskon 20%
# member & belanja < 100000 → diskon 10%
# bukan member → tidak ada diskon

total = float(input('masukkan total belanja: '))
status = input('masukkan status: ')

if total >= 100000 and status == 'ya':
    print('diskon 20%')
elif total < 100000 and status == 'ya':
    print('diskon 10%')
else:
    print('tidak ada diskon')