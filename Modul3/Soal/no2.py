# Terkait matrix dan list comprehension, buatlah (dengan memanfaatkan list comprehension) fungsi-fungsi:
# 1. Untuk membangkitkan matrix berisi nol semua, dengan diberikan ukurannya. Pemanggilan: buatNol(m, n) dan buatNol(m). Pemanggilan dengan
# cara terakhir akan memberikan matrix bujursangkar ukuran m x m.
def buatNol(m, n=None):
    if n == None:
        n = m
    return [[0 for j in range(n)] for i in range(m)]

# 2. Untuk membangkitkan matrix identitas, dengan diberikan ukurannya. Pemanggilan: buatIdentitas(n).
def buatIdentitas(n):
    return [[1 if j == i else 0 for j in range(n)] for i in range(n)]