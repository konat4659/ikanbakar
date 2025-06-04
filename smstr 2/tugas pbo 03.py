import math

# Kelas induk
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Segitiga Sama Kaki
class SegitigaSamaKaki(Segitiga):
    def __init__(self, alas, tinggi):
        super().__init__(alas, tinggi)

    def keliling(self):
        kaki = math.sqrt((self.alas / 2) ** 2 + self.tinggi ** 2)
        return self.alas + 2 * kaki

# Segitiga Siku-siku
class SegitigaSikuSiku(Segitiga):
    def __init__(self, alas, tinggi):
        super().__init__(alas, tinggi)

    def keliling(self):
        miring = math.sqrt(self.alas ** 2 + self.tinggi ** 2)
        return self.alas + self.tinggi + miring

# Segitiga Sama Sisi
class SegitigaSamaSisi(Segitiga):
    def __init__(self, sisi):
        tinggi = (math.sqrt(3) / 2) * sisi
        super().__init__(sisi, tinggi)
        self.sisi = sisi

    def keliling(self):
        return 3 * self.sisi

# Program utama
def main():
    print("1. Segitiga Sama Kaki")
    print("2. Segitiga Siku-Siku")
    print("3. Segitiga Sama Sisi")
    
    pilihan = input("Pilih jenis segitiga (1/2/3): ")

    if pilihan == "1":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        segitiga = SegitigaSamaKaki(alas, tinggi)

    elif pilihan == "2":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        segitiga = SegitigaSikuSiku(alas, tinggi)

    elif pilihan == "3":
        sisi = float(input("Masukkan panjang sisi: "))
        segitiga = SegitigaSamaSisi(sisi)

    else:
        print("Pilihan tidak valid.")
        return

    print("\nHasil Perhitungan:")
    print("Luas     :", segitiga.luas())
    print("Keliling :", segitiga.keliling())

# Menjalankan program
if __name__ == "__main__":
    main()
