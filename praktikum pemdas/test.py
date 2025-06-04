import sqlite3
import os
from faker import Faker
import random
import csv

# Path database
DB_PATH = 'Sistem_University_Academic.db'

# Inisialisasi faker
fake = Faker()

# ===== Fungsi Utilitas =====
def connect_db():
    """
    Membuat koneksi ke database SQLite.
    Mengembalikan objek koneksi atau None jika gagal.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"[ERROR] Koneksi database gagal: {e}")
        return None

def execute_query(query, params=None, fetch=False):
    """
    Eksekusi query SQL dengan parameter opsional.
    - `query`: String query SQL yang akan dijalankan.
    - `params`: Tuple parameter untuk query (default: None).
    - `fetch`: Jika True, mengembalikan hasil query.

    Mengembalikan:
    - Hasil query (jika fetch=True).
    - None jika hanya menjalankan query tanpa fetch.
    """
    params = params or ()
    with connect_db() as conn:
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                if fetch:
                    return cursor.fetchall()
            except sqlite3.Error as e:
                print(f"[ERROR] Kesalahan eksekusi query: {query} | Error: {e}")
                return None
        else:
            print("[ERROR] Tidak dapat terhubung ke database.")
            return None

def initialize_database():
    """
    Inisialisasi database dengan membuat tabel jika belum ada.
    """
    tables = {
        "Prodi": '''
            CREATE TABLE IF NOT EXISTS Prodi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''',
        "User": '''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nim TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'guest',
                prodi_id INTEGER,
                FOREIGN KEY(prodi_id) REFERENCES Prodi(id)
            )
        ''',
        "Matkul": '''
            CREATE TABLE IF NOT EXISTS Matkul (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prodi_id INTEGER,
                FOREIGN KEY(prodi_id) REFERENCES Prodi(id)
            )
        ''',
        "Tugas": '''
            CREATE TABLE IF NOT EXISTS Tugas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matkul_id INTEGER,
                judul TEXT NOT NULL,
                deskripsi TEXT,
                FOREIGN KEY(matkul_id) REFERENCES Matkul(id)
            )
        ''',
        "Jawaban": '''
            CREATE TABLE IF NOT EXISTS Jawaban (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tugas_id INTEGER,
                nim TEXT NOT NULL,
                jawaban TEXT NOT NULL,
                FOREIGN KEY(tugas_id) REFERENCES Tugas(id),
                FOREIGN KEY(nim) REFERENCES User(nim)
            )
        ''',
        "Nilai": '''
            CREATE TABLE IF NOT EXISTS Nilai (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tugas_id INTEGER,
                nim TEXT NOT NULL,
                nilai REAL,
                FOREIGN KEY(tugas_id) REFERENCES Tugas(id),
                FOREIGN KEY(nim) REFERENCES User(nim)
            )
        '''
    }

    for table_name, create_query in tables.items():
        execute_query(create_query)
        print(f"[INFO] Tabel '{table_name}' telah diinisialisasi.")

def reset_database():
    """
    Menghapus file database jika ada dan menginisialisasi ulang database.
    """
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("[INFO] Database lama dihapus.")
    initialize_database()

def insert_dummy_data():
    """
    Menambahkan data dummy ke dalam database.
    - Superuser: Zeta
    - Admin: Astra
    """
    # Tambahkan Superuser dan Admin langsung tanpa menggunakan Faker
    execute_query("INSERT INTO User (nim, name, role) VALUES (?, ?, ?)", ('0000000001', 'Zeta', 'superuser'))
    execute_query("INSERT INTO User (nim, name, role) VALUES (?, ?, ?)", ('1100000001', 'Astra', 'admin'))

    # Generate daftar Program Studi
    base_programs = [
        "Teknik Mesin", "Teknik Elektro", "Teknik Industri", 
        "Teknik Kimia", "Teknik Informatika", "Teknik Sipil",
        "Arsitektur", "Teknologi Industri Pertanian", 
        "Perencanaan Wilayah dan Kota", "Manajemen"
    ]
    program_studi = []
    for program in base_programs:
        for i in range(1, 3):  # Membuat dua entri untuk setiap program
            program_studi.append(f"{program}_{i}")

    # Tambah Program Studi ke database
    for name in program_studi:
        execute_query("INSERT INTO Prodi (name) VALUES (?)", (name,))
    
    # Ambil ID Prodi
    prodi_ids = execute_query("SELECT id FROM Prodi", fetch=True)
    prodi_ids = [row[0] for row in prodi_ids]

    # Tambah Mahasiswa dengan Faker dan berikan nilai acak
    for _ in range(250):
        nim = f"22{str(random.randint(10000000, 99999999))}"
        name = fake.name()
        prodi_id = random.choice(prodi_ids)
        execute_query("INSERT INTO User (nim, name, role, prodi_id) VALUES (?, ?, 'guest', ?)", (nim, name, prodi_id))

        # Memberikan nilai acak antara 65 dan 95 untuk tugas tertentu
        tugas_id = random.randint(1, 250)  # Ambil tugas ID secara acak dari 1 hingga 250
        nilai = random.randint(65, 95)  # Nilai acak antara 65 dan 95

        # Menyimpan nilai ke dalam tabel Nilai
        execute_query("INSERT INTO Nilai (tugas_id, nim, nilai) VALUES (?, ?, ?)", (tugas_id, nim, nilai))

    # Tambah Dosen (tanpa Prodi)
    for _ in range(250):
        nim = f"12{str(random.randint(10000000, 99999999))}"
        name = fake.name()
        execute_query("INSERT INTO User (nim, name, role, prodi_id) VALUES (?, ?, 'guest', NULL)", (nim, name))

    # Tambah Mata Kuliah
    matkul_names = ['Pemrograman Dasar', 'Sistem Basis Data', 'Elektronika Dasar', 'Manajemen Keuangan']
    for _ in range(250):
        name = random.choice(matkul_names)
        prodi_id = random.choice(prodi_ids)
        execute_query("INSERT INTO Matkul (name, prodi_id) VALUES (?, ?)", (name, prodi_id))

    # Tambah Tugas
    for _ in range(250):
        matkul_id = random.randint(1, 250)  # Asumsi ID Matkul sesuai dengan jumlah dummy
        judul = f"Tugas {random.randint(1, 1000)}"
        deskripsi = f"Deskripsi tugas {random.randint(1, 1000)}"
        execute_query("INSERT INTO Tugas (matkul_id, judul, deskripsi) VALUES (?, ?, ?)", (matkul_id, judul, deskripsi))

    print("[INFO] Data dummy berhasil ditambahkan.")

# ===== Fungsi Pagination =====
def paginate_data(data, per_page, page):
    """Membagi data berdasarkan jumlah per halaman dan halaman yang diminta."""
    total_data = len(data)
    total_pages = (total_data + per_page - 1) // per_page
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    if page > total_pages or page < 1:
        return [], total_pages  # Jika halaman di luar jangkauan

    return data[start_index:end_index], total_pages

def display_paginated_data(data, per_page):
    """
    Menampilkan data dengan pagination.
    """
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return

    current_page = 1
    total_pages = (len(data) + per_page - 1) // per_page

    while True:
        # Menampilkan data sesuai halaman
        start_idx = (current_page - 1) * per_page
        end_idx = min(start_idx + per_page, len(data))
        print(f"\n=== Halaman {current_page}/{total_pages} ===")
        for idx, item in enumerate(data[start_idx:end_idx], start=start_idx + 1):
            print(f"{idx}. {item}")

        # Navigasi halaman
        print("\nNavigasi: [P] Sebelumnya | [N] Berikutnya | [E] Keluar")
        choice = input("Pilih opsi: ").strip().lower()

        if choice == 'p' and current_page > 1:
            current_page -= 1
        elif choice == 'n' and current_page < total_pages:
            current_page += 1
        elif choice == 'e':
            break
        else:
            print("Opsi tidak valid.")

# ===== Fungsi untuk Melihat Data =====
def lihat_daftar_pengguna():
    """
    Menampilkan daftar pengguna dengan pagination.
    """
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id, name, nim, role FROM User')
        data = cursor.fetchall()

        per_page = int(input("Berapa banyak data per halaman? (5/10/20/50/100): "))
        display_paginated_data(data, per_page)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def lihat_daftar_matkul():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, prodi_id FROM Matkul')
    data = cursor.fetchall()
    conn.close()

    jumlah_data = int(input("Berapa banyak data yang ingin ditampilkan per halaman? (5/10/20/50/100): "))
    display_paginated_data(data, jumlah_data)

def lihat_daftar_tugas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, judul, deskripsi, matkul_id FROM Tugas')
    data = cursor.fetchall()
    conn.close()

    jumlah_data = int(input("Berapa banyak data yang ingin ditampilkan per halaman? (5/10/20/50/100): "))
    display_paginated_data(data, jumlah_data)

def lihat_daftar_nilai():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, tugas_id, nim, nilai FROM Nilai')
    data = cursor.fetchall()
    conn.close()

    jumlah_data = int(input("Berapa banyak data yang ingin ditampilkan per halaman? (5/10/20/50/100): "))
    display_paginated_data(data, jumlah_data)

def lihat_nilai_persentase():
    """
    Menampilkan nilai persentase mahasiswa berdasarkan tugas yang dikerjakan.
    Hanya mahasiswa dengan role 'guest' yang ditampilkan.
    """
    query = '''
        SELECT 
            User.nim, 
            User.name, 
            SUM(Nilai.nilai) AS total_nilai,
            COUNT(Tugas.id) AS jumlah_tugas
        FROM User
        JOIN Nilai ON User.nim = Nilai.nim
        JOIN Tugas ON Nilai.tugas_id = Tugas.id
        WHERE User.role = 'guest'
        GROUP BY User.nim
    '''
    data = execute_query(query, fetch=True)

    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return

    # Input jumlah data per halaman
    while True:
        try:
            per_page = int(input("Berapa banyak data per halaman? (5/10/20/50/100): "))
            if per_page not in [5, 10, 20, 50, 100]:
                print("Masukkan nilai yang valid dari pilihan yang tersedia (5, 10, 20, 50, 100).")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    current_page = 1
    total_pages = (len(data) + per_page - 1) // per_page  # Total pages

    while True:
        # Menampilkan data untuk halaman tertentu
        paginated_data, total_pages = paginate_data(data, per_page, current_page)

        print("\n=== Daftar Nilai Persentase Mahasiswa ===")
        print(f"{'NIM':<15} {'Nama':<30} {'Persentase Nilai (%)':<20}")
        print("-" * 70)

        for nim, name, total_nilai, jumlah_tugas in paginated_data:
            # Hitung persentase nilai mahasiswa (asumsi nilai maksimal 100 per tugas)
            if jumlah_tugas > 0:
                persentase = (total_nilai / (jumlah_tugas * 100)) * 100
            else:
                persentase = 0
            print(f"{nim:<15} {name:<30} {persentase:<20.2f}")

        print("-" * 70)
        print(f"Halaman {current_page}/{total_pages}")

        # Navigasi halaman
        print("\nNavigasi: [P] Sebelumnya | [N] Berikutnya | [E] Keluar")
        choice = input("Pilih opsi: ").strip().lower()

        if choice == 'p' and current_page > 1:
            current_page -= 1
        elif choice == 'n' and current_page < total_pages:
            current_page += 1
        elif choice == 'e':
            break
        else:
            print("Opsi tidak valid.")

# ===== Fungsi Tambah Data =====
def tambah_pengguna():
    print("\n=== Tambah Pengguna Baru ===")
    nim = input("Masukkan NIM: ").strip()
    nama = input("Masukkan Nama: ").strip()
    prodi_id = input("Masukkan ID Prodi: ").strip()
    role = input("Masukkan Role (superuser/admin/guest): ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO User (nim, nama, prodi_id, role) VALUES (?, ?, ?, ?)',
            (nim, nama, prodi_id, role)
        )
        conn.commit()
        print("Pengguna berhasil ditambahkan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def tambah_matkul():
    print("\n=== Tambah Mata Kuliah Baru ===")
    nama_matkul = input("Masukkan Nama Mata Kuliah: ").strip()
    prodi_id = input("Masukkan ID Prodi: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO Matkul (nama_matkul, prodi_id) VALUES (?, ?)',
            (nama_matkul, prodi_id)
        )
        conn.commit()
        print("Mata Kuliah berhasil ditambahkan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def hapus_matkul():
    matkul_id = input("Masukkan ID mata kuliah yang akan dihapus: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            DELETE FROM Matkul WHERE id = ?
        ''', (matkul_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Mata kuliah berhasil dihapus.")
        else:
            print("ID mata kuliah tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def update_pengguna():
    print("\n=== Update Pengguna ===")
    nim = input("Masukkan NIM pengguna yang akan diupdate: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User WHERE nim = ?', (nim,))
    user = cursor.fetchone()

    if user:
        print(f"Data pengguna saat ini: NIM={user[0]}, Nama={user[1]}, Prodi ID={user[2]}, Role={user[3]}")
        nama_baru = input("Masukkan Nama baru (biarkan kosong untuk tidak mengubah): ").strip()
        prodi_id_baru = input("Masukkan Prodi ID baru (biarkan kosong untuk tidak mengubah): ").strip()
        role_baru = input("Masukkan Role baru (biarkan kosong untuk tidak mengubah): ").strip()

        if nama_baru: user[1] = nama_baru
        if prodi_id_baru: user[2] = prodi_id_baru
        if role_baru: user[3] = role_baru

        cursor.execute(
            'UPDATE User SET nama = ?, prodi_id = ?, role = ? WHERE nim = ?',
            (user[1], user[2], user[3], nim)
        )
        conn.commit()
        print("Pengguna berhasil diperbarui!")
    else:
        print("Pengguna dengan NIM tersebut tidak ditemukan.")
    conn.close()

def hapus_pengguna():
    print("\n=== Hapus Pengguna ===")
    nim = input("Masukkan NIM pengguna yang akan dihapus: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User WHERE nim = ?', (nim,))
    user = cursor.fetchone()

    if user:
        confirm = input(f"Apakah Anda yakin ingin menghapus pengguna dengan NIM={nim}? (y/n): ").strip().lower()
        if confirm == 'y':
            cursor.execute('DELETE FROM User WHERE nim = ?', (nim,))
            conn.commit()
            print("Pengguna berhasil dihapus!")
    else:
        print("Pengguna dengan NIM tersebut tidak ditemukan.")
    conn.close()

# ===== Fungsi Pencarian Data =====
def cari_mahasiswa():
    keyword = input("Masukkan nama atau NIM mahasiswa: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT nim, nama, email, role
            FROM User
            WHERE nim LIKE ? OR nama LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        results = cursor.fetchall()
        if results:
            print("\nHasil Pencarian:")
            print(f"{'NIM':<10} {'Nama':<20} {'Email':<30} {'Role':<10}")
            print("-" * 75)
            for row in results:
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<30} {row[3]:<10}")
        else:
            print("Tidak ada mahasiswa yang cocok dengan kata kunci.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def cari_matkul():
    keyword = input("Masukkan nama mata kuliah: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT id, nama_matkul, sks, semester
            FROM Matkul
            WHERE nama_matkul LIKE ?
        ''', (f'%{keyword}%',))
        results = cursor.fetchall()
        if results:
            print("\nHasil Pencarian:")
            print(f"{'ID':<5} {'Nama Mata Kuliah':<30} {'SKS':<5} {'Semester':<10}")
            print("-" * 60)
            for row in results:
                print(f"{row[0]:<5} {row[1]:<30} {row[2]:<5} {row[3]:<10}")
        else:
            print("Tidak ada mata kuliah yang cocok dengan kata kunci.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

# ===== Fungsi Generate Laporan =====
def laporan_nilai():
    print("\n=== Laporan Nilai Mahasiswa ===")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT 
                User.nim, User.nama, Matkul.nama_matkul, Tugas.nama_tugas, Nilai.nilai
            FROM Nilai
            JOIN User ON Nilai.user_nim = User.nim
            JOIN Tugas ON Nilai.tugas_id = Tugas.id
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
            ORDER BY User.nim, Matkul.nama_matkul, Tugas.nama_tugas
        ''')
        results = cursor.fetchall()
        print(f"{'NIM':<10} {'Nama':<20} {'Mata Kuliah':<30} {'Tugas':<20} {'Nilai':<5}")
        print("-" * 85)
        for row in results:
            print(f"{row[0]:<10} {row[1]:<20} {row[2]:<30} {row[3]:<20} {row[4]:<5}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def update_nilai_mahasiswa():
    nim = input("Masukkan NIM mahasiswa: ").strip()
    tugas_id = input("Masukkan ID tugas: ").strip()
    nilai_baru = input("Masukkan nilai baru: ").strip()

    if not nilai_baru.isdigit() or int(nilai_baru) < 0 or int(nilai_baru) > 100:
        print("Nilai harus berupa angka antara 0 dan 100.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Nilai
            SET nilai = ?
            WHERE user_nim = ? AND tugas_id = ?
        ''', (int(nilai_baru), nim, tugas_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Nilai berhasil diperbarui.")
        else:
            print("Data tidak ditemukan. Periksa NIM dan ID tugas.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def laporan_tugas_matkul():
    print("\n=== Laporan Tugas dan Mata Kuliah ===")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT 
                Matkul.nama_matkul, Tugas.nama_tugas, Tugas.deadline
            FROM Tugas
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
            ORDER BY Matkul.nama_matkul, Tugas.deadline
        ''')
        results = cursor.fetchall()
        print(f"{'Mata Kuliah':<30} {'Nama Tugas':<30} {'Deadline':<20}")
        print("-" * 80)
        for row in results:
            print(f"{row[0]:<30} {row[1]:<30} {row[2]:<20}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def ekspor_nilai_csv():
    print("\n=== Ekspor Nilai ke CSV ===")
    filename = input("Masukkan nama file (tanpa ekstensi): ").strip() + ".csv"
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT 
                User.nim, User.nama, Matkul.nama_matkul, Tugas.nama_tugas, Nilai.nilai
            FROM Nilai
            JOIN User ON Nilai.user_nim = User.nim
            JOIN Tugas ON Nilai.tugas_id = Tugas.id
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
            ORDER BY User.nim, Matkul.nama_matkul, Tugas.nama_tugas
        ''')
        results = cursor.fetchall()
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["NIM", "Nama", "Mata Kuliah", "Tugas", "Nilai"])
            writer.writerows(results)
        print(f"Data berhasil diekspor ke file {filename}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

# ===== Fungsi Utama =====
def login():
    """
    Fungsi login untuk pengguna berdasarkan NIM.
    Memeriksa role pengguna dan mengarahkan ke menu yang sesuai.
    """
    while True:
        print("\n=== Sistem Akademik ===")
        nim = input("Masukkan NIM (atau ketik 'exit' untuk keluar): ").strip()

        if nim.lower() == 'exit':
            print("Keluar dari sistem. Sampai jumpa!")
            break

        # Cek apakah NIM terdaftar
        user_data = execute_query("SELECT name, role FROM User WHERE nim = ?", (nim,), fetch=True)
        if not user_data:
            print("NIM tidak ditemukan. Silakan coba lagi.")
            continue

        name, role = user_data[0]  # Ambil nama dan role pengguna

        print(f"Login berhasil. Selamat datang, {name}!")
        
        # Arahkan ke menu sesuai role
        if role == 'superuser':
            superuser_menu()
        elif role == 'admin':
            admin_menu()
        elif role == 'guest':
            if nim.startswith('22'):  # Mahasiswa
                mahasiswa_menu(nim)
            elif nim.startswith('12'):  # Dosen
                dosen_menu()
            else:
                print("Peran tidak dikenali. Harap periksa kembali NIM Anda.")
        else:
            print("Role tidak dikenali. Hubungi administrator sistem.")

def validasi_role(role):
    role_valid = ['superuser', 'admin', 'guest']
    return role.lower() in role_valid

def validasi_prodi_id(prodi_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM Prodi WHERE id = ?', (prodi_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Lihat Daftar Pengguna")
        print("2. Lihat Daftar Mata Kuliah")
        print("3. Cari Mahasiswa")
        print("4. Cari Mata Kuliah")
        print("5. Lihat Nilai Persentase Mahasiswa")
        print("6. Tambah Pengguna")
        print("7. Tambah Mata Kuliah")
        print("8. Update Pengguna")
        print("9. Update Nilai Mahasiswa")
        print("10. Hapus Pengguna")
        print("11. Hapus Mata Kuliah")
        print("12. Keluar")

        pilihan = input("Pilih opsi: ").strip()
        if pilihan == '1':
            lihat_daftar_pengguna()
        elif pilihan == '2':
            lihat_daftar_matkul()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            cari_matkul()
        elif pilihan == '5': 
            lihat_nilai_persentase()
        elif pilihan == '6':
            tambah_pengguna()
        elif pilihan == '7':
            tambah_matkul()
        elif pilihan == '8':
            update_pengguna()
        elif pilihan == '9':
            update_nilai_mahasiswa()
        elif pilihan == '10':
            hapus_pengguna()
        elif pilihan == '11':
            hapus_matkul()
        elif pilihan == '12':
            print("Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def superuser_menu():
    while True:
        print("\n=== Superuser Menu ===")
        print("1. Lihat Daftar Pengguna")
        print("2. Lihat Daftar Mata Kuliah")
        print("3. Cari Mahasiswa")
        print("4. Cari Mata Kuliah")
        print("5. Lihat Nilai Persentase Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih opsi: ").strip()
        if pilihan == '1':
            lihat_daftar_pengguna()
        elif pilihan == '2':
            lihat_daftar_matkul()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            cari_matkul()
        elif pilihan == '5':
            lihat_nilai_persentase()
        elif pilihan == '6':
            print("Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# ===== Fungsi Dosen =====
def dosen_menu():
    """
    Menu untuk dosen.
    Menyediakan opsi untuk mengelola tugas, memberikan nilai, dan melihat statistik.
    """
    while True:
        print("""
        === Menu Dosen ===
        1. Lihat Daftar Tugas
        2. Tambah Tugas Baru
        3. Berikan Nilai Mahasiswa
        4. Lihat Nilai Persentase
        5. Lihat Statistik Tugas
        6. Keluar
        """)
        choice = input("Pilih opsi (1-6): ").strip()

        if choice == '1':
            lihat_daftar_tugas()
        elif choice == '2':
            tambah_tugas()
        elif choice == '3':
            berikan_nilai_mahasiswa()
        elif choice == '4':
            lihat_nilai_persentase()
        elif choice == '5':
            lihat_statistik_tugas()
        elif choice == '6':
            print("Keluar dari menu dosen.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def lihat_daftar_tugas():
    """
    Menampilkan daftar tugas yang telah dibuat dosen.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT Tugas.id, Matkul.name, Tugas.judul, Tugas.deskripsi
            FROM Tugas
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
        ''')
        hasil = cursor.fetchall()

        if hasil:
            print("\n=== Daftar Tugas ===")
            for tugas in hasil:
                print(f"ID: {tugas[0]} | Mata Kuliah: {tugas[1]} | Judul: {tugas[2]} | Deskripsi: {tugas[3]}")
        else:
            print("Tidak ada tugas yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def tambah_tugas():
    """
    Menambahkan tugas baru untuk mata kuliah tertentu.
    """
    matkul_id = input("Masukkan ID Mata Kuliah: ").strip()
    judul = input("Masukkan Judul Tugas: ").strip()
    deskripsi = input("Masukkan Deskripsi Tugas: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Tugas (matkul_id, judul, deskripsi)
            VALUES (?, ?, ?)
        ''', (matkul_id, judul, deskripsi))
        conn.commit()
        print(f"Tugas '{judul}' berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def berikan_nilai_mahasiswa():
    """
    Memberikan nilai kepada mahasiswa berdasarkan tugas yang dipilih.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Ambil semua tugas
        cursor.execute('''
            SELECT 
                Tugas.id AS id_tugas,
                Matkul.name AS mata_kuliah,
                Tugas.judul AS judul
            FROM Tugas
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
        ''')
        tugas_list = cursor.fetchall()

        if not tugas_list:
            print("Tidak ada tugas yang tersedia untuk dinilai.")
            return

        # Tampilkan daftar tugas
        print("\n=== Daftar Tugas ===")
        print(f"{'ID Tugas':<10} {'Mata Kuliah':<30} {'Judul':<30}")
        print("-" * 70)
        for id_tugas, mata_kuliah, judul in tugas_list:
            print(f"{id_tugas:<10} {mata_kuliah:<30} {judul:<30}")

        # Pilih tugas untuk dinilai
        tugas_id = input("Masukkan ID tugas yang ingin dinilai (atau tekan Enter untuk kembali): ").strip()
        if not tugas_id.isdigit():
            print("ID tugas tidak valid.")
            return

        tugas_id = int(tugas_id)
        selected_task = next((t for t in tugas_list if t[0] == tugas_id), None)

        if not selected_task:
            print("ID tugas tidak ditemukan.")
            return

        # Tampilkan jawaban mahasiswa untuk tugas ini
        cursor.execute('''
            SELECT 
                Jawaban.nim AS nim_mahasiswa,
                User.name AS nama_mahasiswa,
                Jawaban.jawaban AS jawaban
            FROM Jawaban
            JOIN User ON Jawaban.nim = User.nim
            WHERE Jawaban.tugas_id = ?
        ''', (tugas_id,))
        jawaban_list = cursor.fetchall()

        if not jawaban_list:
            print("Tidak ada jawaban yang dikumpulkan untuk tugas ini.")
            return

        print("\n=== Jawaban Mahasiswa ===")
        print(f"{'NIM':<15} {'Nama Mahasiswa':<30} {'Jawaban':<50}")
        print("-" * 100)
        for nim, nama, jawaban in jawaban_list:
            print(f"{nim:<15} {nama:<30} {jawaban:<50}")

        # Pilih mahasiswa untuk diberi nilai
        nim_mahasiswa = input("Masukkan NIM mahasiswa yang ingin diberi nilai: ").strip()
        selected_jawaban = next((j for j in jawaban_list if j[0] == nim_mahasiswa), None)

        if not selected_jawaban:
            print("NIM mahasiswa tidak ditemukan.")
            return

        # Berikan nilai
        nilai = input(f"Masukkan nilai untuk {selected_jawaban[1]} (NIM: {nim_mahasiswa}): ").strip()
        if not nilai.isdigit() or int(nilai) < 0 or int(nilai) > 100:
            print("Nilai harus berupa angka antara 0 hingga 100.")
            return

        nilai = int(nilai)
        cursor.execute('''
            INSERT OR REPLACE INTO Nilai (tugas_id, nim, nilai)
            VALUES (?, ?, ?)
        ''', (tugas_id, nim_mahasiswa, nilai))
        conn.commit()
        print(f"Nilai {nilai} berhasil diberikan kepada {selected_jawaban[1]}.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def lihat_statistik_tugas():
    """
    Menampilkan rata-rata nilai untuk setiap tugas.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT Tugas.judul, AVG(Nilai.nilai)
            FROM Tugas
            LEFT JOIN Nilai ON Tugas.id = Nilai.tugas_id
            GROUP BY Tugas.id
        ''')
        hasil = cursor.fetchall()

        if hasil:
            print("\n=== Statistik Tugas ===")
            for judul, rata_rata in hasil:
                print(f"Tugas: {judul} | Rata-rata Nilai: {rata_rata:.2f}")
        else:
            print("Tidak ada statistik nilai untuk tugas saat ini.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

# ===== Fungsi Mahasiswa =====
def mahasiswa_menu(nim):
    """
    Menu untuk mahasiswa.
    Menyediakan opsi untuk melihat nilai, tugas, dan statistik nilai.
    """
    while True:
        print(f"""
        === Menu Mahasiswa (NIM: {nim}) ===
        1. Lihat Nilai
        2. Lihat Tugas
        3. Kerjakan Tugas
        4. Lihat Statistik Nilai
        5. Keluar
        """)
        choice = input("Pilih opsi (1-5): ").strip()

        if choice == '1':
            lihat_nilai_mahasiswa(nim)
        elif choice == '2':
            lihat_tugas_mahasiswa(nim)
        elif choice == '3':
            mengerjakan_tugas(nim)
        elif choice == '4':
            lihat_statistik_nilai_mahasiswa(nim)
        elif choice == '5':
            print("Keluar dari menu mahasiswa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def lihat_nilai_mahasiswa(nim):
    """
    Menampilkan nilai mahasiswa berdasarkan NIM.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Ambil nilai mahasiswa
        cursor.execute('''
            SELECT 
                Matkul.name AS mata_kuliah,
                Tugas.judul AS tugas,
                Nilai.nilai AS nilai
            FROM Nilai
            JOIN Tugas ON Nilai.tugas_id = Tugas.id
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
            WHERE Nilai.nim = ?
        ''', (nim,))
        hasil = cursor.fetchall()

        if hasil:
            print(f"\n=== Nilai Mahasiswa (NIM: {nim}) ===")
            print(f"{'Mata Kuliah':<30} {'Tugas':<30} {'Nilai':<5}")
            print("-" * 70)
            for mata_kuliah, tugas, nilai in hasil:
                print(f"{mata_kuliah:<30} {tugas:<30} {nilai:<5}")
        else:
            print(f"Belum ada nilai yang tercatat untuk NIM {nim}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def lihat_tugas_mahasiswa(nim):
    """
    Menampilkan tugas yang tersedia untuk mahasiswa berdasarkan NIM.
    Mahasiswa dapat memilih tugas dan menjawabnya.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Ambil semua tugas yang tersedia
        cursor.execute('''
            SELECT 
                Tugas.id AS id_tugas,
                Matkul.name AS mata_kuliah,
                Tugas.judul AS judul,
                Tugas.deskripsi AS deskripsi
            FROM Tugas
            JOIN Matkul ON Tugas.matkul_id = Matkul.id
            WHERE Matkul.id IN (
                SELECT prodi_id FROM User WHERE nim = ?
            )
        ''', (nim,))
        tugas_list = cursor.fetchall()

        if not tugas_list:
            print("Tidak ada tugas yang tersedia untuk Anda.")
            return

        # Tampilkan daftar tugas
        print("\n=== Daftar Tugas ===")
        print(f"{'ID Tugas':<10} {'Mata Kuliah':<30} {'Judul':<30}")
        print("-" * 70)
        for id_tugas, mata_kuliah, judul, _ in tugas_list:
            print(f"{id_tugas:<10} {mata_kuliah:<30} {judul:<30}")

        # Pilih tugas untuk dijawab
        tugas_id = input("Masukkan ID tugas yang ingin dijawab (atau tekan Enter untuk kembali): ").strip()
        if not tugas_id.isdigit():
            print("ID tugas tidak valid.")
            return

        tugas_id = int(tugas_id)
        selected_task = next((t for t in tugas_list if t[0] == tugas_id), None)

        if not selected_task:
            print("ID tugas tidak ditemukan.")
            return

        # Tampilkan detail tugas
        print("\n=== Detail Tugas ===")
        print(f"Mata Kuliah: {selected_task[1]}")
        print(f"Judul      : {selected_task[2]}")
        print(f"Deskripsi  : {selected_task[3]}")

        # Jawab tugas
        jawaban = input("Masukkan jawaban Anda untuk tugas ini: ").strip()
        if not jawaban:
            print("Jawaban tidak boleh kosong.")
            return

        # Simpan jawaban ke database
        cursor.execute('''
            INSERT INTO Jawaban (tugas_id, nim, jawaban)
            VALUES (?, ?, ?)
        ''', (tugas_id, nim, jawaban))
        conn.commit()
        print("Jawaban Anda berhasil disimpan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def mengerjakan_tugas(nim, tugas_id):
    """
    Fungsi untuk mengerjakan tugas yang telah dipilih mahasiswa.
    """
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Tampilkan tugas yang dipilih
        cursor.execute("SELECT judul, deskripsi FROM Tugas WHERE id = ?", (tugas_id,))
        tugas = cursor.fetchone()

        if tugas:
            print(f"\nMengkerjakan Tugas: {tugas[0]}")
            print(f"Deskripsi: {tugas[1]}")
            nilai = input("Masukkan nilai Anda untuk tugas ini (0-100): ")

            try:
                nilai = float(nilai)
                if 0 <= nilai <= 100:
                    # Simpan nilai ke dalam database
                    cursor.execute("""
                        INSERT INTO Nilai (tugas_id, nim, nilai)
                        VALUES (?, ?, ?)
                    """, (tugas_id, nim, nilai))
                    conn.commit()
                    print("Tugas berhasil dikerjakan dan nilai sudah disimpan.")
                else:
                    print("Nilai harus diantara 0 dan 100.")
            except ValueError:
                print("Input nilai tidak valid. Harus berupa angka.")
        else:
            print("Tugas tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

def lihat_statistik_nilai_mahasiswa(nim):
    """
    Menampilkan rata-rata nilai mahasiswa untuk semua tugas.
    """
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT AVG(Nilai.nilai)
            FROM Nilai
            WHERE Nilai.nim = ?
        ''', (nim,))
        rata_rata = cursor.fetchone()[0]

        if rata_rata is not None:
            print(f"Rata-rata nilai Anda: {rata_rata:.2f}")
        else:
            print("Belum ada nilai yang tercatat untuk Anda.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    reset_database()
    initialize_database()
    insert_dummy_data()
    login()

# if __name__ == "__main__":
#     initialize_database()
#     login()