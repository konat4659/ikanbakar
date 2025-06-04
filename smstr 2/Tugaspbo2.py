# Interface
class Interfacehewan:
    def info(self):
        pass
    def bersuara(self):
        pass

# Kelas induk
class Hewan(Interfacehewan):
    def __init__(self, nama, habitat, warna, usia):
        self.nama = nama
        self.habitat = habitat
        self.warna = warna
        self.usia = usia

    def info(self):
        print("Informasi Hewan:")
        print("Nama: ", self.nama)
        print("Habitat: ", self.habitat)
        print("Warna: ", self.warna)
        print("Usia: ", self.usia, "tahun")

    def bersuara(self):
        print(self.nama, "tereak")

# Class turunan dari Hewan
class Air(Hewan):
    def __init__(self, nama, habitat, warna, usia, berenang=True):
        super().__init__(nama, habitat, warna, usia)
        self.berenang = berenang

    def info(self):
        super().info()
        print("Berenang: ", "Ya" if self.berenang else "Tidak")

# Class turunan dari Air
class RajaLele(Air):
    def __init__(self, nama, habitat, warna, usia, ras):
        super().__init__(nama, habitat, warna, usia)
        self.ras = ras

    def info(self):  # diperbaiki dari 'indo' jadi 'info'
        super().info()
        print("Ras: ", self.ras)

    def bersuara(self):
        print(self.nama, "tereak: buajdingan")

# Data dan output
rajaLele1 = RajaLele('kondro', 'air terjun', 'maghrib', 3, 'Sejarah')
rajaLele2 = RajaLele('kond', 'air terjun', 'maghrib', 2, 'Sejarah')
rajaLele3 = RajaLele('konro', 'air terjun', 'maghrib', 4, 'Sejarah')

print("=== Data RajaLele ===")
for rajalele in [rajaLele1, rajaLele2, rajaLele3]:
    rajalele.info()
    rajalele.bersuara()
    print("-" * 30)
