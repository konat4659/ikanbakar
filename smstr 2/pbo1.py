class MATAKULIAH:
    def __init__(self, hari, matkul, jam):
        self.hari = hari
        self.matkul = matkul
        self.jam = jam
    
    def tampilkan_info(self):
        print(f"Hari: {self.hari}")
        print(f"Matkul: {self.matkul}")
        print(f"Jam: {self.jam}")

# Membuat objek dari kelas Mahasiswa
matakuliah1 = MATAKULIAH("Senin", "Statistika", "09.00")
matakuliah2 = MATAKULIAH("Selasa", "Agama Islam", "09.40")

# Menampilkan informasi mahasiswa
matakuliah1.tampilkan_info()
print("--------------------")
matakuliah2.tampilkan_info()