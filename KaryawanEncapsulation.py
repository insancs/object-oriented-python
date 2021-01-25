# class Karyawan:
#     nama_perusahaan = "ABC"
#     __insentif_lembur = 250000
#
#     def __init__(self, nama, usia, pendapatan):
#         self.__nama = nama
#         self.__usia = usia
#         self.__pendapatan = pendapatan
#         self.__pendapatan_tambahan = 0
#
#     def lembur(self):
#         self.__pendapatan_tambahan += self.__insentif_lembur
#
#     def tambahan_proyek(self, insentif_proyek):
#         self.__pendapatan_tambahan += insentif_proyek
#
#     def total_pendapatan(self):
#         return self.__pendapatan_tambahan + self.__pendapatan
#
#
# # Akses ke attribute class Karyawan
# insan = Karyawan("Insan", 24, 8500000)
# # insan.tambahan_proyek(insan.__insentif_lembur) # Menghasilkan error karena __insentif_lembur bersifat private
# insan.lembur()
# insan.lembur()
# print(insan.total_pendapatan())

class Karyawan:
    nama_perusahaan = 'ABC'
    __insentif_lembur = 250000

    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__pendapatan_tambahan = 0

    def lembur(self):
        insentif_lembur = self.__insentif_lembur
        if self.__usia > 30:
            insentif_lembur *= 2
        self.__pendapatan_tambahan += insentif_lembur

    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan += insentif_proyek

    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan


karyawan_1 = Karyawan('Kiki', 35, 8000000)
karyawan_1.lembur()
karyawan_1.tambahan_proyek(220000)
print(karyawan_1.total_pendapatan())
