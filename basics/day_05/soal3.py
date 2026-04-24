# soal 3

# Belanja + Bonus

# Input total belanja:

# jika ≥ 100000 → dapat bonus
# jika ≥ 200000 → bonus besar
# selain itu → bonus kecil
# jika < 100000 → tidak ada bonus

total = float(input('masukkan total: '))

if total >= 100000:
    print('dapat bonus')
    
    if total >= 200000:
        print('bonus besar')
    else:
        print('bonus kecil')
else:
    print('tidak ada bonus')