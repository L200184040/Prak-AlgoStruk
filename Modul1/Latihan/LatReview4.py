from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a) # mengubah jenis integer menjadi float
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D < 0: # memeriksa apakah determinan D bernilai negatif
        real = -b / (2 * a)
        imajiner = akar(-D) / (2 * a)
        x1 = complex(real, imajiner)
        x2 = complex(real, -imajiner)
    else:
        x1 = (-b + akar(D)) / (2 * a)
        x2 = (-b - akar(D)) / (2 * a)
    hasil = (x1,x2) # tuple yang terdiri atas dua elemen
    return hasil