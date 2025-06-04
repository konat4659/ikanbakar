# Contoh dictionary
mahasiswa = {
    "nama": "John Doe",
    "umur": 21,
    "jurusan": "Teknik Informatika"
}

print(mahasiswa["nama"])  # Output: John Doe
print(mahasiswa["jurusan"])  # Output: Teknik Informatika

# Menambahkan data ke dictionary
mahasiswa["semester"] = 5
print(mahasiswa)

mahasiswa.pop("nama")
print(mahasiswa)