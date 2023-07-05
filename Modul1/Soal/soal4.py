def rerata(a):
    jumlah = 0
    for i in a:
        jumlah += i
    return jumlah/len(a)
def variance(a):
    jumlah = 0
    for i in a:
        jumlah += (i - rerata(a))**2
    return jumlah/(len(a)-1)
def stdDev(a):
    return variance(a)**0.5
a = input('Masukkan bilangan: ')
a = a.split(',')
a = [int(i) for i in a]
def jalankan(a):
    print('Rerata: ', rerata(a))
    print('Variansi: ', variance(a))
    print('Standar deviasi: ', stdDev(a))
jalankan(a)