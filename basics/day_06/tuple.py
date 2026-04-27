# tuple mirip dengan list tapi bedanya tuple tidak bisa di ubah-ubah datanya

kordinat = (20.1, -10.2)
rgb = (255, 128, 0)
satu_elemen = (1,)
tanpa_kurung = 1, 2, 3

print(kordinat)
print(rgb)
print(satu_elemen)
print(tanpa_kurung)

# tuple unpacking
x, y = kordinat

print(f'Latitude: {x}', f'Langitude: {y}')

r, g, b = rgb
print(f'r: {r}', f'g: {g}', f'b: {b}')

# swap variable
a, b = 24, 7
a, b = b, a
print(a, b)