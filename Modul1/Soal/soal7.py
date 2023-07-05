def faktorPrima(n):
    faktor = []
    i = 2
    while i <= n:
        if n % i == 0:
            faktor.append(i)
            n = n / i
        else:
            i += 1
    faktor = tuple(faktor)
    return faktor