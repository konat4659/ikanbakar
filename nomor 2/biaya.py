# transportasi/biaya.py

def hitung_biaya(kendaraan_tipe, jarak):
    if kendaraan_tipe.lower() == "mobil":
        biaya = jarak * 5000
    elif kendaraan_tipe.lower() == "motor":
        biaya = jarak * 3000
    else:
        return "Tipe kendaraan tidak dikenal."
    
    return biaya