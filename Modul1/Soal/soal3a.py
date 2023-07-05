def jumlahHurufVokal(x):
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for i in x:
        if i in vokal:
            jumlah +=1
    jumlah=(len(x),jumlah)
    return jumlah