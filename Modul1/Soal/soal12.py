import random
a = random.randint(1,100)
b = 0
nyawa = 5

print("Permainan tebak angka.")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
while b != a:
    b = int(input("Masukkan tebakan ke-{}: ".format(6-nyawa) + "> "))
    if b > a:
        print("Itu terlalu besar. Coba lagi")
    elif b < a:
        print("Itu terlalu kecil. Coba lagi")
    else:
        print("Ya. Anda benar")
        break
    nyawa -= 1
    if nyawa == 0:
        print("Anda kalah. Angka yang saya pilih adalah {}".format(a))
        break