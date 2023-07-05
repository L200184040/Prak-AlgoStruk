def apakahKabisat():
    tahun = int(input("Masukkan tahun: "))
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                print("Tahun kabisat")
            else:
                print("Bukan tahun kabisat (meski habis dibagi 4, tapi habis dibagi 100 dan tidak habis dibagi 400)")
        else:
            print("Tahun kabisat")
    else:
        print("Bukan tahun kabisat")
while True:
    apakahKabisat()
    print("Apakah Anda ingin mengulanginya? (y/n)")
    ulang = input()
    if ulang == "n":
        break
    elif ulang == "y":
        continue
    else:
        print("Input tidak valid")
        break