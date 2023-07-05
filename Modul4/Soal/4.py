from lat2 import *

def uangSakuKurang(daftar):
    list = []
    for i in daftar:
        if i.uangSaku < 250000:
            list.append(i)
    return list

print(uangSakuKurang(Daftar))