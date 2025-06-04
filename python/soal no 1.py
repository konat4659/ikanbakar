class Mahasiswa:
    def _init_(self, nama, golongan, ciri):
        self.nama = nama
        self.golongan = golongan
        self.ciri = ciri

def main():
    mahasiswa_list = []

    print("Masukan informasi mahasiswa:")

    for i in range(5):
        golongan = i + 1
        print(f"\nMahasiswa {golongan}")
        nama = input("Masukan nama: ")
        ciri = input("Masukan ciri: ")
        mahasiswa_list.append(Mahasiswa(nama, golongan, ciri))

    print("\nTampilkan Informasi:\n")

    for i, mhs in enumerate(mahasiswa_list, start=1):
        print(f"\nMahasiswa: {i}")
        print(f"Nama: {mhs.nama}")
        print(f"Ciri ciri: {mhs.ciri}")

if __name__ == "__main__":
    main()