# peminjaman.py
from .buku import buku_list

peminjaman_list = []

def pinjam_buku(judul, nama_peminjam):
    for buku in buku_list:
        if buku['judul'] == judul:
            if buku['status'] == 'dipinjam':
                return f"Buku '{judul}' sudah dipinjam."
            buku['status'] = 'dipinjam'
            peminjaman_list.append({'judul': judul, 'nama_peminjam': nama_peminjam})
            return f"Buku '{judul}' berhasil dipinjam oleh {nama_peminjam}."
    return f"Buku '{judul}' tidak ditemukan."

def kembalikan_buku(judul):
    for buku in buku_list:
        if buku['judul'] == judul and buku['status'] == 'dipinjam':
            buku['status'] = 'tersedia'
            peminjaman_list[:] = [p for p in peminjaman_list if p['judul'] != judul]
            return f"Buku '{judul}' berhasil dikembalikan."
    return f"Buku '{judul}' tidak sedang dipinjam."
