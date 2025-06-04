class Pegawai:
    def __init__(self, nama, id_pegawai):
        self.nama = nama
        self.id_pegawai = id_pegawai
    
    def hitung_gaji(self):
        pass

class PegawaiTetap(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_tetap):
        super().__init__(nama, id_pegawai)
        self.gaji_tetap = gaji_tetap
    
    def hitung_gaji(self):
        return self.gaji_tetap

class PegawaiKontrak(Pegawai):
    def __init__(self, nama, id_pegawai, upah_per_jam, jam_kerja):
        super().__init__(nama, id_pegawai)
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    
    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

def main():
    pegawai_tetap = [
        PegawaiTetap("Andi", "PT001", 5000000),
        PegawaiTetap("Budi", "PT002", 4500000),
    ]

    pegawai_kontrak = [
        PegawaiKontrak("Cici", "PK001", 50000, 160),
        PegawaiKontrak("Dedi", "PK002", 60000, 150),
    ]

    print("=== Pegawai Tetap ===")
    for p in pegawai_tetap:
        print(f"Nama: {p.nama}, ID: {p.id_pegawai}, Gaji: Rp{p.hitung_gaji():,}")

    print("\n=== Pegawai Kontrak ===")
    for p in pegawai_kontrak:
        gaji = p.hitung_gaji()
        print(f"Nama: {p.nama}, ID: {p.id_pegawai}, Upah per Jam: Rp{p.upah_per_jam:,}, Jam Kerja: {p.jam_kerja} jam, Total Gaji: Rp{gaji:,}")

if __name__ == "__main__":
    main()
        