from LatOOP3 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIM,kota,us,lk=[]):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.lk = lk
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah
    def listKuliah(self):
        return self.lk
    def ambilKuliah(self, ambil):
        self.lk.append(ambil)
    def hapusMatkul(self, hapus):
        for i in self.lk:
            if hapus in self.lk:
                self.lk.remove(hapus)
            else:
                print('Mata kuliah tidak dapat dihapus karena tidak ada dalam daftar mata kuliah yang diambil.')
    
""" a = input("Masukkan Nama: ")
b = input("Masukkan NIM: ")
c = input("Masukkan Kota Tinggal: ")
d = input("Masukkan Uang Saku: ")
x = Mahasiswa(a,b,c,d)
print('Data Mahasiswa: ',x) """

m1 = Mahasiswa('Gunawan',194,'Karanganyar',270000)
# ada kelanjutannya (lihat di "Soal-soal untuk Mahasiswa").