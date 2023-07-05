from lat2 import *

def urutkanNIM(Daftar):
    n = len(Daftar)
    for i in range(n-1):
        for j in range(n-i-1):
            if Daftar[j].NIM > Daftar[j+1].NIM:
                Daftar[j], Daftar[j+1] = Daftar[j+1], Daftar[j]

print('Sebelum diurutkan:')
print('NIM'.ljust(10), 'Nama'.ljust(10), 'Kota'.ljust(12), 'Uang Saku'.ljust(10))
for i in Daftar:
    nim = str(i.NIM)
    nama = str(i.nama)
    kota = str(i.kotaTinggal)
    uang_saku = str(i.uangSaku)
    print(nim.ljust(10), nama.ljust(10), kota.ljust(12), uang_saku.ljust(10))

urutkanNIM(Daftar)
print('\nSetelah diurutkan:')
print('NIM'.ljust(10), 'Nama'.ljust(10), 'Kota'.ljust(12), 'Uang Saku'.ljust(10))
for i in Daftar:
    nim = str(i.NIM)
    nama = str(i.nama)
    kota = str(i.kotaTinggal)
    uang_saku = str(i.uangSaku)
    print(nim.ljust(10), nama.ljust(10), kota.ljust(12), uang_saku.ljust(10))