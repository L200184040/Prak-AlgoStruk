x = int(input('Masukkan tinggi siku-siku: '))
def cetakSiku(x):
    for i in range(1, x+1):
        for j in range(1, i+1):
            print('*', end='')
        print()
cetakSiku(x)