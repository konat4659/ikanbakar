# Kelas Produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"- {self.nama} | Harga: Rp{self.harga} | Stok: {self.stok}")

# Kelas Karyawan
class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def tampilkan_info(self):
        print(f"- {self.nama} ({self.jabatan})")

# Kelas Supermarket (umum)
class Supermarket:
    def __init__(self, nama, lokasi):
        self.nama = nama
        self.lokasi = lokasi
        self.karyawan = []
        self.produk = []

    def tambah_karyawan(self, karyawan):
        self.karyawan.append(karyawan)

    def tambah_produk(self, produk):
        self.produk.append(produk)

    def tampilkan_info(self):
        print(f"\nSupermarket: {self.nama}")
        print(f"Lokasi: {self.lokasi}")
        print("\nDaftar Karyawan:")
        for k in self.karyawan:
            k.tampilkan_info()
        print("\nDaftar Produk:")
        for p in self.produk:
            p.tampilkan_info()
        print()

# Kelas Supermarket Pusat (Hubungan ke Cabang)
class SupermarketPusat(Supermarket):
    def __init__(self, nama, lokasi):
        super().__init__(nama, lokasi)
        self.cabang = []

    def tambah_cabang(self, supermarket_cabang):
        self.cabang.append(supermarket_cabang)

    def tampilkan_struktur(self):
        print(f"\nSupermarket Pusat: {self.nama}")
        print(f"Lokasi: {self.lokasi}")
        print(f"Jumlah Cabang: {len(self.cabang)}")
        for cabang in self.cabang:
            cabang.tampilkan_info()

# --- Contoh Penggunaan ---

# Supermarket Pusat
pusat = SupermarketPusat("SuperMart Pusat", "Jakarta")

# Supermarket Cabang
cabang1 = Supermarket("SuperMart Cabang Bandung", "Jl. Asia Afrika No.10")
cabang2 = Supermarket("SuperMart Cabang Surabaya", "Jl. Basuki Rahmat No.25")

# Tambah Karyawan dan Produk ke Cabang
cabang1.tambah_karyawan(Karyawan("Budi", "Kepala Toko"))
cabang1.tambah_karyawan(Karyawan("Rina", "Kasir"))
cabang1.tambah_produk(Produk("Beras 5kg", 60000, 50))
cabang1.tambah_produk(Produk("Minyak Goreng 1L", 15000, 100))

cabang2.tambah_karyawan(Karyawan("Doni", "Kepala Toko"))
cabang2.tambah_produk(Produk("Gula 1kg", 14000, 70))
cabang2.tambah_produk(Produk("Tepung Terigu 1kg", 12000, 80))

# Tambah Cabang ke Pusat
pusat.tambah_cabang(cabang1)
pusat.tambah_cabang(cabang2)

# Tampilkan Struktur Supermarket
pusat.tampilkan_struktur()
