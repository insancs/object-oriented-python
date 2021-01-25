# Definisikan class Karyawan (sebagai base class)
class Karyawan():
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = 250000

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan


# Buat class turunan (sebagai inherit class) dari class karyawan, yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        # melakukan pemanggilan konstruktur class Karyawan
        super().__init__(nama, usia, pendapatan)


# Buat kembali class turunan (sebagai inherit class) dari class karyawan, yaitu class IlmuwanData
class IlmuwanData(Karyawan):

    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

    # Pendefinisian kembali function lembur dari class Karyawan termasuk polymorphism
    def lembur(self):
        # Pendapatan uang lembur sebesar 10% dari pendapatannya
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)


# Buat objek karyawan yang bekerja sebagai AnalisData
insan = AnalisData("Insan Cahya Setia", 24, 4500000)
insan.lembur()
insan.tambahan_proyek(100000)
print("Total Pendapatan Insan :", insan.total_pendapatan())

# Buat objek karyawan yang bekerja sebagai IlmuwanData
eunha = IlmuwanData("Jung Eunbi", 23, 6500000)
eunha.lembur()
print("Total Pendapatan Eunha :", eunha.total_pendapatan())

