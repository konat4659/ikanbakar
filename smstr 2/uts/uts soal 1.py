# Import modul random untuk isi array
import random

# Inisialisasi variabel array 3D A[5][6][6]
A = [[[random.uniform(1, 100) for k in range(6)] for j in range(6)] for i in range(5)]

# Fungsi untuk cetak isi array dan alamat simulasi
def tampilkan_array_dan_alamat(array, base_address=5000, byte_per_float=4):
    address = base_address
    print("Isi array dan alamat memori (simulasi):\n")
    for i in range(len(array)):
        for j in range(len(array[i])):
            for k in range(len(array[i][j])):
                print(f"A[{i}][{j}][{k}] = {array[i][j][k]:.2f} \tAlamat: {address}")
                address += byte_per_float

# a. Cetak isi array sebelum mapping
print("a. Isi array sebelum mapping:\n")
tampilkan_array_dan_alamat(A)

# (Simulasi mapping = tidak ada perubahan konten, hanya proses akses, jadi cetak ulang sama)
print("\nIsi array sesudah mapping (sama, hanya traversal ulang):\n")
tampilkan_array_dan_alamat(A)
