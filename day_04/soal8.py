# soal 8

# ATM Sederhana 🔥

# Input:

# saldo
# tarik uang

# Aturan:

# tarik > saldo → "saldo tidak cukup"
# tarik ≤ saldo → tampilkan sisa saldo

saldo = float(input('masukkan saldo: '))
tarik =float(input('masukkan uang: '))

if saldo >= tarik:
    nilai = saldo - tarik
    print('sisa saldo', nilai)
else:
    print('sisa saldo anda',  saldo)