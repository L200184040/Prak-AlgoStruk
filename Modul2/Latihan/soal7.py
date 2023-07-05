from LatOOP4 import Mahasiswa
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

# Dari class Manusia:
# 1. nama
# 2. keadaan
# 3. ucapkanSalam()
# 4. makan()
# 5. olahraga()
# 6. mengalikanDenganDua()
#
# Dari class Mahasiswa:
# 1. nama
# 2. nim
# 3. kotaTinggal
# 4. uangSaku
# 5. ambilNama()
# 6. ambilNIM()
# 7. ambilUangSaku()
# 8. makan()
# 9. ambilKotaTinggal()
# 10. perbaruiKotaTinggal()
# 11. tambahUangSaku()
#
# Dari class MhsTIF:
# katakanPy()

m1 = Mahasiswa('Jamil', 123, 'Sukoharjo', 240000)

# m1.ambilKotaTinggal()
# m1.perbaruiKotaTinggal('Solo')
# m1.ambilUangSaku()
# m1.tambahUangSaku(50000)
# m1.ambilUangSaku()