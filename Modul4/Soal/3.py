from lat2 import *

def uangSakuTerkecil(daftar):
    terkecil = daftar[0].uangSaku
    list = []
    for i in daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            list.append(i)
    return list

print(uangSakuTerkecil(Daftar))