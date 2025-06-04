class RuangRapat:
    def __init__(self, nama, kapasitas, fasilitas):
        self.nama = nama
        self.kapasitas = kapasitas
        self.fasilitas = fasilitas
        self.tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Sudah Dipesan"
        return f"{self.nama} - Kapasitas: {self.kapasitas}, Fasilitas: {', '.join(self.fasilitas)} - {status}"


class Reservasi:
    def __init__(self, pegawai, ruang, waktu):
        self.pegawai = pegawai
        self.ruang = ruang
        self.waktu = waktu

    def __str__(self):
        return f"{self.pegawai} memesan {self.ruang.nama} pada {self.waktu}"


class SistemReservasi:
    def __init__(self):
        self.ruang_list = []
        self.reservasi_list = []

    def tambah_ruang(self, ruang):
        self.ruang_list.append(ruang)

    def tampilkan_ruang(self):
        print("\nDaftar Ruang Rapat:")
        for ruang in self.ruang_list:
            print("-", ruang)

    def reservasi_ruang(self, pegawai, nama_ruang, waktu):
        for ruang in self.ruang_list:
            if ruang.nama.lower() == nama_ruang.lower() and ruang.tersedia:
                reservasi = Reservasi(pegawai, ruang, waktu)
                self.reservasi_list.append(reservasi)
                ruang.tersedia = False
                print(f"\n✅ Reservasi berhasil untuk {pegawai} pada {waktu} di ruang {ruang.nama}.")
                return
        print("\n❌ Ruang tidak tersedia atau tidak ditemukan.")

    def batalkan_reservasi(self, pegawai, nama_ruang):
        for reservasi in self.reservasi_list:
            if reservasi.pegawai.lower() == pegawai.lower() and reservasi.ruang.nama.lower() == nama_ruang.lower():
                reservasi.ruang.tersedia = True
                self.reservasi_list.remove(reservasi)
                print(f"\n❎ Reservasi {nama_ruang} oleh {pegawai} dibatalkan.")
                return
        print("\n⚠️ Reservasi tidak ditemukan.")

    def tampilkan_reservasi(self):
        print("\nDaftar Reservasi Aktif:")
        if not self.reservasi_list:
            print("Belum ada reservasi.")
        else:
            for res in self.reservasi_list:
                print("-", res)


# ============================
# Simulasi penggunaan sistem
# ============================

sistem = SistemReservasi()

# Tambahkan ruang rapat
sistem.tambah_ruang(RuangRapat("Ruang Kecil", 5, ["TV", "AC"]))
sistem.tambah_ruang(RuangRapat("Ruang Sedang", 10, ["TV", "AC", "Papan Tulis"]))
sistem.tambah_ruang(RuangRapat("Ruang Besar", 20, ["Proyektor", "Sound System", "Mic", "AC"]))

# Menu interaktif sederhana
while True:
    print("\n=== Sistem Reservasi Ruang Rapat ===")
    print("1. Lihat Ruang")
    print("2. Reservasi Ruang")
    print("3. Batalkan Reservasi")
    print("4. Lihat Reservasi Aktif")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        sistem.tampilkan_ruang()

    elif pilihan == "2":
        pegawai = input("Nama pegawai: ")
        nama_ruang = input("Nama ruang yang ingin dipesan: ")
        waktu = input("Waktu reservasi (contoh: 10.00 - 12.00): ")
        sistem.reservasi_ruang(pegawai, nama_ruang, waktu)

    elif pilihan == "3":
        pegawai = input("Nama pegawai: ")
        nama_ruang = input("Nama ruang yang ingin dibatalkan: ")
        sistem.batalkan_reservasi(pegawai, nama_ruang)

    elif pilihan == "4":
        sistem.tampilkan_reservasi()

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
