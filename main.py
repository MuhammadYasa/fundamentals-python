# Contruction Python
# sequentials : eksekusi sesuai urutan
# semua eksekusi yang dilakukan sesuai urutan dari atas sampai kebawah
print('Nama : Muhammad Yasa')
print('Tempat lahir : Surabaya')
print('Kebangsaan : Indonesia')
print('Tanggal saat ini : 17 Juni 2020')
print('---' * 20)

# percabangan : dengan syarat
orang_sehat = True
if orang_sehat:
    print('olah raga & istirahat teratur')
else:
    print('makan junkfood dan bermalas malasan')

print('---' * 20)
# Perulangan

jumlah_rumah = 5

for index_rumah in range(1, jumlah_rumah+1): # jumlah perulangannya dimulai nomor pertama terus di tambah satu data hinga data yang terakhir
    print(f'Alamat Rumah #{index_rumah}') # f berguna untuk melakukan print terhadap variabel