import csv
from datetime import datetime

# Membaca data penjualan
def baca_data_penjualan(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Menghitung total penjualan per produk
def hitung_total_penjualan(file_path):
    data = baca_data_penjualan(file_path)
    hasil = {}
    for row in data:
        id_produk = row[1]
        jumlah = int(row[3])
        harga = int(row[4])
        if id_produk in hasil:
            hasil[id_produk] += jumlah * harga
        else:
            hasil[id_produk] = jumlah * harga
    return hasil

# Menyaring data berdasarkan tanggal
def filter_berdasarkan_tanggal(file_path, tanggal):
    data = baca_data_penjualan(file_path)
    hasil = [row for row in data if row[0] == tanggal]
    return hasil

# Menambahkan data penjualan
def tambah_data_penjualan(file_path, data_baru):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_baru)

# Contoh penggunaan
file_path = "data_penjualan.csv"
tanggal_filter = "2024-01-01"
data_baru = ["2024-01-02", "P003", "Produk Baru", 10, 50000]

print("Membaca Data:", baca_data_penjualan(file_path))
print("Total Penjualan:", hitung_total_penjualan(file_path))
print("Filter Berdasarkan Tanggal:", filter_berdasarkan_tanggal(file_path, tanggal_filter))
tambah_data_penjualan(file_path, data_baru)
