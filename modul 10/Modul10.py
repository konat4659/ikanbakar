import pandas as pd

# Membaca dataset
data = pd.read_csv("data.csv")

# Menampilkan data
print("Data:")
print(data)

# Statistik Deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())

# Korelasi antara Usia dan Penghasilan
korelasi = data["Usia"].corr(data["Penghasilan"])
print(f"\nKorelasi antara Usia dan Penghasilan: {korelasi:.2f}")