from transportasi import (
    tambah_kendaraan,
    tampilkan_kendaraan,
    tambah_rute,
    tampilkan_rute,
    hitung_biaya,
    kendaraan_data,
)

# Menambahkan kendaraan
tambah_kendaraan("Toyota", "Avanza", 2020, "Mobil")
tambah_kendaraan("Honda", "CBR", 2022, "Motor")

# Menambahkan rute perjalanan
tambah_rute("Toyota Avanza", "Jakarta", "Bandung", 150)
tambah_rute("Honda CBR", "Surabaya", "Malang", 100)

# Menampilkan kendaraan dan rute perjalanan
print("\nDaftar Kendaraan:")
tampilkan_kendaraan()

print("\nDaftar Rute:")
tampilkan_rute()

# Menghitung dan menampilkan biaya perjalanan
print("\nBiaya Perjalanan:")
for rute in rute_list:
    kendaraan_obj = next((k for k in kendaraan_list if str(k) == rute['kendaraan']), None)
    if kendaraan_obj:
        biaya = hitung_biaya(kendaraan_obj, rute['jarak'])
        print(f"Kendaraan: {rute['kendaraan']}, Biaya: {biaya}")