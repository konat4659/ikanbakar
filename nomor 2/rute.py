# transportasi/rute.py

class Rute:
    def __init__(self, asal, tujuan, jarak):
        self.asal = asal
        self.tujuan = tujuan
        self.jarak = jarak

class ManajemenRute:
    def __init__(self):
        self.rute_list = []

    def tambah_rute(self, asal, tujuan, jarak):
        rute = Rute(asal, tujuan, jarak)
        self.rute_list.append(rute)

    def tampilkan_rute(self):
        for rute in self.rute_list:
            print(f"Asal: {rute.asal}, Tujuan: {rute.tujuan}, Jarak: {rute.jarak} km")