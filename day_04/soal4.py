# soal 4

# Login + Status
# username & password benar → login berhasil
# username benar tapi password salah → password salah
# username salah → username tidak ditemukan

user= 'dale'
pw = '11'

u = input('masukkan username: ')
p = input('masukkan password: ')

if u == user and p == pw:
    print('login berhasil')
elif u == user and p != pw:
    print('password salah')
else:
    print('username tidak ditemukan')