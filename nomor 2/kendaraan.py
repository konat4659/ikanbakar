# transportasi/kendaraan.py

class Kendaraan:
    def __init__(self, merek, model, tahun, tipe):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.tipe = tipe

class ManajemenKendaraan:
    def __init__(self):
        self.kendaraan_list = []

    def tambah_kendaraan(self, merek, model, tahun, tipe):
        kendaraan = Kendaraan(merek, model, tahun, tipe)
        self.kendaraan_list.append(kendaraan)

    def tampilkan_kendaraan(self):
        for kendaraan in self.kendaraan_list:
            print(f"Merek: {kendaraan.merek}, Model: {kendaraan.model}, Tahun: {kendaraan.tahun}, Tipe: {kendaraan.tipe}")