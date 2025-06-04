import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a. Simulasikan data selama 30 hari
np.random.seed(0)  # Untuk reproduktifitas
days = 30
hours = np.arange(0, 24)  # Jam dari 0 hingga 23
data = []

for day in range(days):
    for hour in hours:
        kecepatan_rata_rata = np.random.randint(40, 101)  # Kecepatan antara 40 dan 100 km/jam
        jumlah_kendaraan = np.random.randint(100, 1001)  # Jumlah kendaraan antara 100 dan 1000
        data.append([day, hour, kecepatan_rata_rata, jumlah_kendaraan])

# b. Ubah array ke DataFrame menggunakan Pandas
df = pd.DataFrame(data, columns=['Hari', 'Jam', 'Kecepatan_Rata-rata', 'Jumlah_Kendaraan'])

# c. Analisis
# Hitung rata-rata kecepatan berdasarkan jam
rata_rata_kecepatan = df.groupby('Jam')['Kecepatan_Rata-rata'].mean()

# Tentukan waktu dengan kepadatan lalu lintas tertinggi
jam_kepadatan_tertinggi = df.groupby('Jam')['Jumlah_Kendaraan'].sum().idxmax()

# d. Buat visualisasi data ke dalam bentuk line chart
plt.figure(figsize=(14, 7))

# Plot kecepatan rata-rata
plt.subplot(2, 1, 1)
plt.plot(rata_rata_kecepatan.index, rata_rata_kecepatan.values, marker='o', color='b', label='Kecepatan Rata-rata')
plt.title('Rata-rata Kecepatan Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Kecepatan Rata-rata (km/jam)')
plt.xticks(hours)
plt.grid()
plt.legend()

# Plot jumlah kendaraan
jumlah_kendaraan_per_jam = df.groupby('Jam')['Jumlah_Kendaraan'].sum()
plt.subplot(2, 1, 2)
plt.plot(jumlah_kendaraan_per_jam.index, jumlah_kendaraan_per_jam.values, marker='o', color='r', label='Jumlah Kendaraan')
plt.title('Jumlah Kendaraan Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Kendaraan')
plt.xticks(hours)
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig('visualisasi_lalu_lintas.pdf')  # Simpan grafik ke PDF
plt.show()

# e. Simpan hasil ke file CSV
df.to_csv('data_lalu_lintas.csv', index=False)

# Output hasil analisis
print("Rata-rata kecepatan berdasarkan jam:")
print(rata_rata_kecepatan)
print("\nJam dengan kepadatan lalu lintas tertinggi:", jam_kepadatan_tertinggi)