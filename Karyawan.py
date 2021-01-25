# Definisikan class Karyawan
class Karyawan():
    nama_perusahaan = 'Startup Corporation'
    # insentif_lembur bisa juga dimasukkan ke parameter __init__
    insentif_lembur = 250000

    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan


# inisialisasi object yang dinyatakan dalam variabel insan dan cahya
insan = Karyawan("Insan Cahya S", 24, 4500000)
eunha = Karyawan("Jung Eunbi", 23, 6500000)
# insan melaksanakan lembur
insan.lembur()
# eunha mendapat proyek
eunha.tambahan_proyek(2500000)


# Definisikan class Perusahaan
class Perusahaan():
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []

    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.append(karyawan)

    def nonaktif_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = karyawan
                break
            if karyawan_nonaktif is not None:
                self.list_karyawan.remove(karyawan_nonaktif)


# Definisikan object perusahaan
perusahaan = Perusahaan("ABC", "Kp. Giri Mukti No 06 RT 02 RW 20", "085723523213")

# Definisikan nama-nama karyawan
karyawan1 = Karyawan("Jung Yerin", 24, 7500000)
karyawan2 = Karyawan("Kim Sowon", 25, 8500000)
karyawan3 = Karyawan("Hwang Eunbi", 22, 4000000)

# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan1)
perusahaan.aktifkan_karyawan(karyawan2)
perusahaan.aktifkan_karyawan(karyawan3)

# Cetak nama perusahaan melalui penggunaan keyword __class__ pada class attribute nama_perusahaan
print(insan.__class__.nama_perusahaan)
print(eunha.__class__.nama_perusahaan)

# Penggabungan bisa menggunakan koma atau operator + (khusus str)
print("Nama\t:", insan.nama, "\nUsia\t: " + str(insan.usia), "\nPendapatan\t:", insan.pendapatan)
print("Pendapatan total :", insan.total_pendapatan())
print("Nama\t:", eunha.nama, "\nUsia\t: " + str(eunha.usia), "\nPendapatan\t:", eunha.pendapatan)
print("Pendapatan total : " + str(eunha.total_pendapatan()))
