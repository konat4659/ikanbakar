# main.py
from perpustakaan import tambah_buku, hapus_buku, cari_buku, update_buku
from perpustakaan import pinjam_buku, kembalikan_buku
from perpustakaan import daftar_buku, laporan_peminjaman

# Menambahkan buku
tambah_buku("Pemrograman Python untuk Pemula", "Sugeng Winardi", 2023)
tambah_buku("Langkah Mudah Belajar Machine Learning", "Randi Adrika Putra", 2021)
print(tambah_buku("AI Revolution", "Elon Smith", 2019))
print()

# Meminjam buku
print(pinjam_buku("Pemrograman Python untuk Pemula", "Rania"))
print(pinjam_buku("AI Revolution", "Adrian"))
print()

# Menampilkan laporan
print("Daftar Buku:", daftar_buku())
print("Laporan Peminjaman:", laporan_peminjaman())
print()

# Mengembalikan buku
print(kembalikan_buku("Pemrograman Python untuk Pemula"))
print()

# Menampilkan laporan setelah pengembalian
print("Daftar Buku Setelah Pengembalian:", daftar_buku())
print()
