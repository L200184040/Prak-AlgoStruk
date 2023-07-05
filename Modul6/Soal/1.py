from oop import *

def mergeSort(A):
    print("Membelah     ", [str(x) for x in A])
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0
        j = 0
        k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].ambilNIM() < separuhKanan[j].ambilNIM():
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1

    print("Menggabungkan", [str(x) for x in A])

# Contoh penggunaan
mhs1 = MhsTIF('John Doe', 12345, 'Jakarta', 1500000)
mhs2 = MhsTIF('Jane Smith', 67890, 'Bandung', 2000000)
mhs3 = MhsTIF('Alice Johnson', 54321, 'Surabaya', 1800000)

alist = [mhs1, mhs2, mhs3]
mergeSort(alist)

for mhs in alist:
    print(mhs)