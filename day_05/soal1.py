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

u = 'admin'
p = '12'

user = input('masukkan username: ')
pw = input('masukkan password: ')

if user == u and pw == p:
  print('selamat datang admin')
  
  if user !='admin':
      print('selamat datang user')
  else:
      print('login gagal')

else:
   print('login gagal')
