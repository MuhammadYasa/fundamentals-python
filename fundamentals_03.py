"""
tipe data dictionary dapat menghubungkan antara key dan value
KVP = Key Value Pair
"""

kamus_indo_english = {}   # perbedaan dict dan list, adalah kalau dict menggunakan kurung kurawal {}
kamus_indo_english['harimau'] = 'tiger'
kamus_indo_english['gajah'] = 'elephant'
kamus_indo_english['kucing'] = 'cat'
kamus_indo_english['anjing'] = 'dog'

print(kamus_indo_english)
print(kamus_indo_english['gajah'])
print(kamus_indo_english['anjing'])


try:
    d = print(kamus_indo_english['dog'])
    if print(kamus_indo_english['dog']) == 'anjing':
        print(d.text)  # mencetak isi halaman dari request diatas
except Exception as e:
    print('Have a problem',e)
#dictionary hanya satu arah, kalau ingin mencetak dari nilai ke key nya, harus mendeklarasikan dari kedua sisinya

print('Data ini ditampilkan untuk informasi penduduk')
data_dari_server_dispenduk = {
    'tanggal' : '2020-06-17',
    'nama_penduduk' : [
        {'Nama': 'Muhammad','Kekayaan': '10'},
        {'Nama': 'Yasa','Kekayaan': '100'},
        {'Nama': 'Fatimah','Kekayaan': '30'},
        {'Nama': 'Aisyah','Kekayaan': '60'}
    ]
}
print(data_dari_server_dispenduk)
print(f"nama penduduk di area surabaya {data_dari_server_dispenduk['nama_penduduk']}")
print(f"nama penduduk pertama #1 : {data_dari_server_dispenduk['nama_penduduk'][0]}")
print(f"nama penduduk pertama #3 : {data_dari_server_dispenduk['nama_penduduk'][2]}")
print(f"Kekayaan penduduk #2 : {data_dari_server_dispenduk['nama_penduduk'][1]['Kekayaan']} Juta")
