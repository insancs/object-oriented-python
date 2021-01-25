"""Polymorphism"""


# Definisikan class Karyawan (sebagai base class)
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan


# Definisikan class TenagaLepas sebagai child class dari class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)

    def tambahan_proyek(self, insentif_proyek):
        # Insentif proyek TenagaLepas sebesat 1% dari total insentif_proyek
        self.pendapatan_tambahan += int(insentif_proyek * 0.01)


# Definisikan class AnalisData sebagai child class dari class Karyawan
class AnalisData(Karyawan):
    pass


# Definisikan class IlmuwanData sebagai child class dari class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, insentif_proyek):
        # Insentif proyek IlmuwanData sebesat 10% dari total insentif_proyek
        self.pendapatan_tambahan += insentif_proyek * 0.1


# Definisikan class PembersihData sebagai child class dari class TenagaLepas
class PembersihData(TenagaLepas):
    pass


# Definisikan class DokumenterData sebagai child class dari class TenagaLepas
class DokumenterData(TenagaLepas):
    def tambahan_proyek(self, insentif_proyek):
        # DokumenterData tidak mendapatkan pendapatan dari proyek
        return


'''
Contoh Overloading pada Python
Mengizinkan sekumpulan fungsi yg sama dengan parameter yang berbeda
'''


class Overloading(Karyawan):
    # Definisikan parameter usia dan pendapatan berbeda dengan class parent
    def __init__(self, nama, usia=29, pendapatan=1000000):
        super().__init__(nama, usia, pendapatan, 0)


print(">>>[1] Karyawan")
insan = Karyawan('Insan Cahya', 24, 3500000, 100000)
insan.tambahan_proyek(200000)
insan.lembur()
print("Nama : " + insan.nama, "\nUsia : " + str(insan.usia), "\nPendapatan : " + str(insan.pendapatan),
      "\nInsentif Lembur: " + str(insan.insentif_lembur))
print("Total Pendapatan :", insan.total_pendapatan())

print("\n>>>[2] Analis Data")
yerin = AnalisData('Jung Yerin', 25, 5000000, 100000)
yerin.lembur()
yerin.tambahan_proyek(300000)
print("Nama :", yerin.nama, "\nUsia :", yerin.usia, "\nPendapatan :", yerin.pendapatan, "\nInsentif Lembur :",
      yerin.insentif_lembur)
print("Total Pendapatan :", yerin.total_pendapatan())

print("\n>>>[3] Tenaga Lepas")
sinb = TenagaLepas("Hwang Eunbi", 22, 3000000)
sinb.tambahan_proyek(1000000)
print("Nama :", sinb.nama, "\nUsia :", sinb.usia, "\nPendapatan :", sinb.pendapatan, "\nInsentif Lembur:",
      sinb.insentif_lembur)
print("Total Pendapatan :", sinb.total_pendapatan())

print("\n>>>[4] OverLoading")
umji = Overloading('Kim Yewon', pendapatan=1200000)
# Usia di set dengan nilai default
print("Nama :", umji.nama, "\nUsia :", umji.usia, "\nPendapatan :", umji.pendapatan, "\nInsentif Lembur :",
      umji.insentif_lembur)
umji.tambahan_proyek(100000)
print("Total Pendapatan :", umji.total_pendapatan())
