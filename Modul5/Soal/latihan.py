def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):        # lakukan operasi gelembung sebanyak n-1
        for j in range(n-i-1):  # dorong elemen terbesar ke ujung kanan
            if A[j] > A[j+1]:   # jika di kiri lebih besar dari kanannya,
                swap(A,j,j+1)   # tukar posisi elemen ke j dengan ke j+1

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:   # -> Cari posisi yang tepat
            A[pos] = A[pos - 1]                 #    dan geser ke kanan terus
            pos = pos - 1                       #    nilai - nilai yang lebih besar
        A[pos] = nilai # -> Pada posisi ini ditempatkan nilai elemen ke i