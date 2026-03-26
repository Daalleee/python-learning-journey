# soal 5 

#  Login Level 2 
# username benar & password benar → login berhasil
# username benar & password salah → password salah
# username salah → username tidak ditemukan

user = 'dale'
pw = '2407'

input1 = input('masukkan username: ')
input2 = input('masukkan password: ')

if input1 == user and input2 == pw:
    print('berhasil login')
elif not input1 == user and input2 == pw:
    print('login gagal')
else:
    print('login gagal')