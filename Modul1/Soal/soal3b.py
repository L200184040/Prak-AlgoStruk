def jumlahHurufKonsonan(x):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    jumlah = 0
    for i in x:
        if i in konsonan:
            jumlah +=1
    jumlah=(len(x),jumlah)
    return jumlah