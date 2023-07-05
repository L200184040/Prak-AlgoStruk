from lat2 import *

def uangSakuTerkecil(daftar):
    terkecil = daftar[0].uangSaku
    for i in daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil

print(uangSakuTerkecil(Daftar))