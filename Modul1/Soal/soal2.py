tinggi = int(input('Masukkan tinggi persegi empat: '))
lebar = int(input('Masukkan lebar persegi empat: '))
def gambarlahPersegiEmpat(tinggi, lebar):
    for i in range(1, tinggi+1):
        for j in range(1, lebar+1):
            if i == 1 or i == tinggi or j == 1 or j == lebar:
                print('@', end='')
            else:
                print(' ', end='')
        print()
gambarlahPersegiEmpat(tinggi, lebar)