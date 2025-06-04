class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.status = "tersedia"

    def pinjam(self):
        if self.status == "tersedia":
            self.status = "dipinjam"
            return True
        return False

    def kembalikan(self):
        self.status = "tersedia"

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang} - {self.status}"


class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id = id_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_dipinjam.append(buku)
            print(f"{self.nama} meminjam '{buku.judul}'.")
        else:
            print(f"Buku '{buku.judul}' sedang tidak tersedia.")

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.kembalikan()
            self.buku_dipinjam.remove(buku)
            print(f"{self.nama} mengembalikan '{buku.judul}'.")
        else:
            print(f"{self.nama} tidak meminjam buku itu.")


# Data awal
daftar_buku = [
    Buku("Siksa Kubur", "Ibnu Rajab"),
    Buku("Ingin Jadi Kaya Tapi Malas", "Raja Ikan"),
    Buku("100 Cara Jadi Sigma", "El Semule")
]

daftar_anggota = []

# Fungsi pencarian
def cari_buku(judul):
    for buku in daftar_buku:
        if buku.judul.lower() == judul.lower():
            return buku
    return None

def cari_anggota(nama):
    for anggota in daftar_anggota:
        if anggota.nama.lower() == nama.lower():
            return anggota
    return None

# Menu utama
while True:
    print("\n=== Menu Perpustakaan ===")
    print("1. Daftar Anggota Baru")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Lihat Daftar Buku")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama anggota: ")
        id_anggota = input("Masukkan ID anggota: ")
        if cari_anggota(nama):
            print("Anggota dengan nama ini sudah terdaftar.")
        else:
            daftar_anggota.append(Anggota(nama, id_anggota))
            print(f"Anggota '{nama}' berhasil didaftarkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama anggota: ")
        anggota = cari_anggota(nama)
        if not anggota:
            print("Anggota tidak ditemukan. Silakan daftar terlebih dahulu.")
            continue
        judul = input("Masukkan judul buku yang ingin dipinjam: ")
        buku = cari_buku(judul)
        if buku:
            anggota.pinjam_buku(buku)
        else:
            print("Buku tidak ditemukan.")

    elif pilihan == "3":
        nama = input("Masukkan nama anggota: ")
        anggota = cari_anggota(nama)
        if not anggota:
            print("Anggota tidak ditemukan.")
            continue
        judul = input("Masukkan judul buku yang ingin dikembalikan: ")
        buku = cari_buku(judul)
        if buku:
            anggota.kembalikan_buku(buku)
        else:
            print("Buku tidak ditemukan.")

    elif pilihan == "4":
        print("\nDaftar Buku:")
        for buku in daftar_buku:
            print(f"- {buku}")
        if not daftar_buku:
            print("Belum ada buku.")

    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
