import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a. Buat dataset dengan 100 individu
np.random.seed(0)  # Untuk reproduktifitas
n_individu = 100

# b. Variabel yang dibutuhkan
usia = np.random.randint(18, 91, size=n_individu)  # Usia antara 18 dan 90
pendapatan = np.random.randint(3000000, 20000001, size=n_individu)  # Pendapatan antara 3 juta dan 20 juta
tingkat_pendidikan = np.random.choice(['SMA', 'Diploma', 'Sarjana', 'Magister', 'Doktor'], size=n_individu)

# Membuat DataFrame
data = {
    'Usia': usia,
    'Pendapatan': pendapatan,
    'Tingkat_Pendidikan': tingkat_pendidikan
}
df = pd.DataFrame(data)

# c. Analisis
# Hitung pendapatan rata-rata berdasarkan tingkat pendidikan
rata_rata_pendapatan = df.groupby('Tingkat_Pendidikan')['Pendapatan'].mean().reset_index()

# Kelompokkan data berdasarkan kelompok usia
bins = [18, 30, 50, 65, 90]
labels = ['18-30', '31-50', '51-65', '66-90']
df['Kelompok_Usia'] = pd.cut(df['Usia'], bins=bins, labels=labels, right=True)

# Hitung rata-rata pendapatan berdasarkan kelompok usia
rata_rata_pendapatan_usia = df.groupby('Kelompok_Usia')['Pendapatan'].mean().reset_index()

# d. Visualisasikan dengan matplotlib
plt.figure(figsize=(14, 7))

# Visualisasi pendapatan rata-rata berdasarkan tingkat pendidikan
plt.subplot(2, 1, 1)
plt.bar(rata_rata_pendapatan['Tingkat_Pendidikan'], rata_rata_pendapatan['Pendapatan'], color='skyblue')
plt.title('Pendapatan Rata-rata Berdasarkan Tingkat Pendidikan')
plt.xlabel('Tingkat Pendidikan')
plt.ylabel('Pendapatan Rata-rata (Rp)')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Visualisasi pendapatan rata-rata berdasarkan kelompok usia
plt.subplot(2, 1, 2)
plt.bar(rata_rata_pendapatan_usia['Kelompok_Usia'], rata_rata_pendapatan_usia['Pendapatan'], color='salmon')
plt.title('Pendapatan Rata-rata Berdasarkan Kelompok Usia')
plt.xlabel('Kelompok Usia')
plt.ylabel('Pendapatan Rata-rata (Rp)')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.tight_layout()
plt.savefig('visualisasi_demografi.pdf')  # Simpan grafik ke PDF
plt.show()

# e. Simpan hasil ke file CSV
df.to_csv('data_demografi.csv', index=False)

# Output hasil analisis
print("Pendapatan Rata-rata Berdasarkan Tingkat Pendidikan:")
print(rata_rata_pendapatan)
print("\nPendapatan Rata-rata Berdasarkan Kelompok Usia:")
print(rata_rata_pendapatan_usia)