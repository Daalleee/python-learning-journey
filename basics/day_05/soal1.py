# soal 1

# Login + Role

# Input:

# username
# password

# Jika login benar:

# jika username = admin → tampilkan "selamat datang admin"
# selain itu → "selamat datang user"

# Jika login salah:

# "login gagal"

u = 'dale'
p = '12'

user = input('masukkan username: ')
pw = input('masukkan password: ')

if pw == p and (user == 'admin' or user == u):
    if user == 'admin':
        print('selamat datang admin')
    else:
        print('selamat datang user')
else:
    print('login gagal')