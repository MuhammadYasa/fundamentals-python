# Tipe data skalar > Simple
rumah1 = 'surabaya'
rumah2 = 'sidoarjo'
rumah3 = 'gresik'
rumah4 = 'pasuruan'

print(rumah1)
print(rumah2)
print(rumah3)
print(rumah4)

# tipe data list/array
# rumah = []
# rumah.append('surabaya')
# rumah.append('sidoarjo')
# rumah.append('gresik')
# rumah.append('pasuruan')
# print(rumah)
# cara diatas cara yang terlalu lama, dan kurang efisien kalau harus menambahkan data banyak secara sekaligus

rumah = ['surabaya', 'sidoarjo', 'gresik', 'pasuruan']

print('\n')
print(rumah)

rumah.append('malang')
print('\n')
print(rumah)
print('\n')

# untuk mencetak rumah ke 3
print(f'alamat rumah ke 3 : {rumah[4]}')  # index ketika pemanggilan di mulai dari yang pertama = 0
print('\n')

# perulangan yang di khususkan untuk list
for r in rumah:
    print(f'alamat rumah {r}!')

# cara perulangan yang terlalu panjang pengetikannya
for r in range(0, len(rumah)):  # len(rumah) menghitung sampai berapa saja nilai yg terkandung dalam rumah
    print(f'{r + 1}. alamat rumah {rumah[r]}')  # {r+1}. = melakukan print angka urutannya,
