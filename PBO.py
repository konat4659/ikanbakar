class perusahaan:
    def __init__(self, Nama, NO_HP, Kelamin, Divisi):
        self.nama = Nama
        self.no_hp = NO_HP
        self.kelamin = Kelamin
        self.divisi = Divisi
    def Info(self):
        self.Info = f"Nama {self.nama} Nomor Hpnya {self.no_hp} Jenis kelaminnya {self.kelamin} divisinya {self.divisi}"
        return self.Info
    
pekerja = []
jumlah = int(input("Masukkan banyaknya pekerja : "))
for i in range (jumlah):
    nama = input("Masukkan nama pekerja: ")
    no_hp = int(input("Masukkan no hp pekerja: "))
    kelamin = (input("Masukkan kelamin: "))
    divisi = (input("Masukkan divisi: "))
    p = perusahaan(nama, no_hp, kelamin,divisi )
    pekerja.append(p)

for p in pekerja:
    print("\npekerja: ", p.nama)
    print(p.Info())
    