from datetime import date
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku",self.nama)
    def makan(self,s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan",k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self,nama,NISN,umur,kota,us):
        self.nama = nama
        self.NISN = NISN
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NISN ' + str(self.NISN) \
            + '. Umur ' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap harinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.NISN
    def ambilUmur(self):
        return self.umur
    def tahunLahir(self):
        return date.today().year - self.umur
    def ambilUangSaku(self):
        return self.uangSaku
    