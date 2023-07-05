def quickSort(A):
    quickSortBantu(A,0,len(A)-1) # Memanggil quickSortBantu dengan parameter

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)      # Atur elemen dan dapatkan titikBelah
        quickSortBantu(A, awal, titikBelah - 1)   # Ini rekursi untuk belah sisi kiri
        quickSortBantu(A, titikBelah + 1, akhir)  # dan belah sisi kanan.

def partisi(A,awal,akhir):
    nilaiPivot = A[awal]    # Di sini nilaiPivot kita ambil dari elemen yang paling kiri.

    penandaKiri = awal + 1  # Posisi awal penandaKiri
    penandaKanan = akhir    # Posisi awal penandaKanan

    selesai = False
    while not selesai:  # loop di bawah adalah untuk mengatur ulang posisi semua elemen

        while penandaKiri <= penandaKanan and \
                A[penandaKiri] <= nilaiPivot:       # penandaKiri bergerak ke kanan, sampai ketemu suatu nilai yang
            penandaKiri = penandaKiri + 1           # lebih besar dari nilaiPivot

        while A[penandaKanan] >= nilaiPivot and \
                penandaKanan >= penandaKiri:        # penandaKanan bergerak ke kiri, sampai ketemu suatu nilai yang
            penandaKanan = penandaKanan - 1         # lebih kecil dari nilaiPivot

        if penandaKanan < penandaKiri:              # Kalau dua penanda sudah bersilangan,
            selesai = True                          # selesai & lanjut ke penempatan pivot
        else:
            temp = A[penandaKiri]                   # Tapi kalau belum bersilangan, 
            A[penandaKiri] = A[penandaKanan]        # tukarlah isi yang ditunjuk oleh
            A[penandaKanan] = temp                  # penandaKiri dan penandaKanan

    temp = A[awal]              # Kalau acara tukar menukar posisi sudah selesai,
    A[awal] = A[penandaKanan]   # kita lalu menempatkan pivot pada posisi yang tepat,
    A[penandaKanan] = temp      # yakni posisi penandaKanan.
                                # Posisi penandaKanan adalah juga titikBelah.
    return penandaKanan     # Fungsi ini mengembalikan titikBelah ke pemanggil