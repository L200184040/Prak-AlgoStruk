# 1. Untuk memastikan bahwa isi dan ukuran matrix-nya konsisten (karena tiap anggota dari list-luar-nya bisa saja mempunyai ukuran \
#    yang berbeda-beda. Dan bahkan bisa saja berbeda tipe!).
def apakahKonsisten(matrix):
    if len(matrix) == 0:
        return True
    else:
        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix[0]):
                return False
        return True

# 2. Untuk mengambil ukuran matrixnya.
def ukuran(matrix):
    if apakahKonsisten(matrix):
        return (len(matrix), len(matrix[0]))
    else:
        return False

# 3. Untuk menjumlahkan dua matrix (pastikan ukurannya sesuai).
def jumlah(matrix1, matrix2):
    if ukuran(matrix1) == ukuran(matrix2):
        hasil = []
        for i in range(len(matrix1)):
            hasil.append([])
            for j in range(len(matrix1[i])):
                hasil[i].append(matrix1[i][j] + matrix2[i][j])
        return hasil
    else:
        return False

# 4. Untuk mengalikan dua matrix (pastikan ukurannya sesuai).
def kali(matrix1, matrix2):
    if ukuran(matrix1)[1] == ukuran(matrix2)[0]:
        hasil = []
        for i in range(ukuran(matrix1)[0]):
            hasil.append([])
            for j in range(ukuran(matrix2)[1]):
                hasil[i].append(0)
                for k in range(ukuran(matrix1)[1]):
                    hasil[i][j] += matrix1[i][k] * matrix2[k][j]
        return hasil
    else:
        return False

# 5. Untuk menghitung determinan sebuah matrix bujursangkar.
def determinan(matrix):
    if ukuran(matrix)[0] == ukuran(matrix)[1]:
        if len(matrix) == 1:
            return matrix[0][0]
        else:
            hasil = 0
            for i in range(len(matrix)):
                hasil += matrix[0][i] * (-1)**(i) * determinan(submatrix(matrix, 0, i))
            return hasil
    else:
        return False