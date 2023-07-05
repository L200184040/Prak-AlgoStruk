from lat2 import *

def cari_mahasiswa(daftar, kota):
    list_index = []
    for i in range(len(daftar)):
        if daftar[i].kotaTinggal == kota:
            list_index.append(i)
    return list_index

print(cari_mahasiswa(Daftar, 'Klaten'))
