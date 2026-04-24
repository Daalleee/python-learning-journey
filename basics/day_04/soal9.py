# soal 9

# Login + Attempt

# Input:

# username
# password

# Aturan:

# benar → "login berhasil"
# salah → "login gagal"

# Bonus:
# tampilkan "coba lagi" (tanpa loop dulu)

user = 'dale'
pw = '12'

u = input('masukkan username: ')
p = input('masukkan password: ')

if u == user and p == pw:
    print('login berhasil')
else:
    print('login gagal')

