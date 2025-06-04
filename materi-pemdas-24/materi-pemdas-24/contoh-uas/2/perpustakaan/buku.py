# buku.py
buku_list = []

def tambah_buku(judul, penulis, tahun):
    if any(buku['judul'] == judul for buku in buku_list):
        return "Buku sudah ada."
    buku_list.append({'judul': judul, 'penulis': penulis, 'tahun': tahun, 'status': 'tersedia'})
    return "Buku berhasil ditambahkan."

def hapus_buku(judul):
    global buku_list
    buku_list = [buku for buku in buku_list if buku['judul'] != judul]
    return f"Buku '{judul}' berhasil dihapus."

def cari_buku(judul):
    for buku in buku_list:
        if buku['judul'] == judul:
            return buku
    return "Buku tidak ditemukan."

def update_buku(judul, penulis=None, tahun=None):
    for buku in buku_list:
        if buku['judul'] == judul:
            if penulis:
                buku['penulis'] = penulis
            if tahun:
                buku['tahun'] = tahun
            return "Buku berhasil diperbarui."
    return "Buku tidak ditemukan."
