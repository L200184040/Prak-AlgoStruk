from lat2 import *

def cari(daftar, dicari):
    list = []
    for i in daftar:
        if i.nama == dicari:
            list.append(i)
    return list

print(cari(Daftar, 'Budi'))