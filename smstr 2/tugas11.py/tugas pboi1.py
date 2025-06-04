class persegi:
    def __init__(self, Nama, Sisi):
        self.nama = Nama
        self.sisi = Sisi
      
        

    def leuas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi
    
    def info(self):
        return f"{self.nama} dengan sisi {self.sisi}"
daftar_bangun = []
jumlah = int(input("Masukkan sisi persegi : "))

for i in range (jumlah):
    print(f"\input data bangun ke-{i+1}")
    nama = input("Masukkan nama bangun: ")
    sisi = float(input{"sisi: "})
  
    bangun = persegi(nama, sisi )
    daftar_bangun.append(bangun)

print("\n== informasi bangun persegi")
for bangun in daftar_bangun:
    print(bangun.info())
    print('luas:', bangun.luas())
 