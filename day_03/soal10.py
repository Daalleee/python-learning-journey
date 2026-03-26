# soal 10

# Menu Sederhana 🔥🔥

# Input pilihan:
# 1 → tambah
# 2 → kurang
# 3 → kali
# 4 → bagi

# Lalu input 2 angka → tampilkan hasil sesuai pilihan

pilih = int(input('masukkan pilihan: 1(tambah), 2(kurang), 3(kali), 4(bagi): '))
nilai1 = int(input('masukkan angaka: '))
nilai2 = int(input('masukkan angaka: '))

if pilih == 1:
    nilai = nilai1 + nilai2
    print(nilai)
elif pilih == 2:
    nilai = nilai1 - nilai2
    print(nilai)
elif pilih == 3:
    nilai = nilai1 * nilai2
    print(nilai)
elif pilih == 4:
    nilai = nilai1 / nilai2
    print(nilai)
else:
    print('harap masukkan yang sesuai')