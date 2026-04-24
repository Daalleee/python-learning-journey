# soal 5
# Login + Attempt 

# Input username & password:

# Jika salah:

# tampilkan "login gagal"
# tampilkan "coba lagi"

# Jika benar:

# tampilkan "login berhasil"
# jika admin → tampilkan "akses penuh"

username = 'halo'
password = '11'

user = input('masukkan username: ')
pw = input('masukkan password: ')

if (user == 'admin' or user == 'halo') and pw == password:
    print('login berhasil')
    
    if user == 'admin':
        print('akses penuh')
else:
    print('login gagal')
    print('coba lagi')