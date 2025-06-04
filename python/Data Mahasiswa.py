def menu():
    print("DATA MAHASISWA")
    print("1. Tambah Mahasiswa")
    print("2. Hapus Mahasiswa")
    print("3. cari data mahasiswa menurut NIM")
    print("4. cari data mahasiswa menurut Nama")
    print("5. cari data mahasiswa menurut Jurusan")
    print("6. Cetak Seluruh data Mahasiswa")
    print("7. selesai")

def tambah_siswa(data):
    nama = input("Masukkan nama siswa: ")
    nim = int(input("Masukkan nim siswa: "))
    umur = input("Masukkan umur siswa: ")
    data[nama] = umur
    print(f"Siswa {nama} berhasil ditambahkan.")

def hapus_siswa(data):
    nama = input("Masukkan nama siswa yang akan dihapus: ")
    if nama in data:
        del data[nama]
        print(f"Siswa {nama} berhasil dihapus.")
    else:
        print("Siswa tidak ditemukan.")

def MahasiswaMRTNIM(data):
    if data:
        print("\nDaftar Mahasiswa Menurut NIM: ")
        for nama, umur in data.items():
            print(f"Nama: {nama}, Umur: {umur}")
    else:
        print("Tidak ada data siswa.")

def main():
    data_siswa = {}
    while True:
        menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tambah_siswa(data_siswa)
        elif pilihan == '2':
            hapus_siswa(data_siswa)
        elif pilihan == '3':
            MahasiswaMRTNIM(data_siswa)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
