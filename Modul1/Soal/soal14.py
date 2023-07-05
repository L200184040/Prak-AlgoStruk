def formatRupiah(x):
    x = str(x)
    if len(x) <= 3:
        return 'Rp ' + x
    else:
        return formatRupiah(x[:-3]) + '.' + x[-3:]