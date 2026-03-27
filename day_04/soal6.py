# soal 6 

# Hari & Cuaca

# Input:

# hari
# cuaca

# Aturan:

# sabtu/minggu & cerah → "pergi jalan"
# sabtu/minggu & hujan → "di rumah"
# hari kerja → "kerja"


hari = input('masukkan hari: ')
cuaca = input('masukkan cuaca: ')

if (hari == 'sabtu' or 'minggu' ) and cuaca =='cerah':
    print('pergi jalan')
elif hari == 'sabtu' or 'minggu':
    print('di rumah')
else:
    print('kerja')