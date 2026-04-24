#soal 5
# SOAL 5 — Login Sederhana 
# username = "admin"
# password = "123"

# Jika benar → "login berhasil"
# Jika salah → "login gagal"

username = 'admin'
password = '123'

login1 = input('masukkan username: ')
login2 = input('masukkan password: ')

if login1 == username and login2 == password:
    print ('login berhasil')
else:
    print('login gagal')