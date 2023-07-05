import math # import modul math

n = 1000 # n adalah batas bilangan prima yang dicari
List = list(range(2, n)) # list berisi bilangan dari 2 sampai n

p = 2 # p adalah bilangan prima pertama

while not int(math.sqrt(p)) + 1 > n: # loop akan berhenti jika akar kuadrat dari p lebih besar dari n

    for x in range(p * 2, n, p): # loop akan mengubah semua bilangan yang merupakan kelipatan dari p menjadi 0
        List[x - 2] = 0 # karena list dimulai dari 2, maka index dari list harus dikurangi 2

    p += 1 # assign p ke bilangan prima selanjutnya

    while p - 2 < len(List) and List[p - 2] == 0: # loop untuk mengecek apakah p sudah menjadi bilangan prima atau belum
        p += 1 # jika p bukan bilangan prima, maka p akan diassign ke bilangan prima selanjutnya

for x in List: # loop untuk menampilkan bilangan prima
    if x != 0: # jika x tidak sama dengan 0, maka x adalah bilangan prima
        print(x) # menampilkan bilangan prima