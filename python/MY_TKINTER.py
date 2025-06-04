import tkinter as tk
import random

# Variabel skor
skor = 0

# Fungsi gerakan bola dengan keyboard
def gerak_kiri(event):
    """Menggerakkan bola ke kiri."""
    canvas.move(bola, -20, 0)  # Geser bola ke kiri
    cek_batas()
    efek_berkilau()

def gerak_kanan(event):
    """Menggerakkan bola ke kanan."""
    canvas.move(bola, 20, 0)  # Geser bola ke kanan
    cek_batas()
    efek_berkilau()

# Cek agar bola tetap dalam batas kanvas
def cek_batas():
    """Mencegah bola keluar dari batas kanvas."""
    x1, y1, x2, y2 = canvas.coords(bola)
    if x1 < 0:
        canvas.move(bola, 20, 0)  # Jika keluar kiri, geser ke kanan
    if x2 > 400:
        canvas.move(bola, -20, 0)  # Jika keluar kanan, geser ke kiri

# Efek bola berkilauan
def efek_berkilau():
    """Efek bola berkilauan dengan mengubah warnanya sesaat."""
    warna_awal = canvas.itemcget(bola, "fill")
    canvas.itemconfig(bola, fill="yellow")
    canvas.after(100, lambda: canvas.itemconfig(bola, fill=warna_awal))

# Buat efek gelombang
def efek_gelombang(x, y):
    """Buat animasi gelombang memancar dari lokasi tabrakan."""
    for i in range(10):
        r = i * 3
        efek_id = canvas.create_oval(x - r, y - r, x + r, y + r, outline="red", width=2)
        canvas.after(i * 50, canvas.delete, efek_id)

# Buat efek rintangan melompat
def efek_rintangan_melompat():
    """Efek ketika rintangan melompat saat muncul."""
    for i in range(5):
        canvas.move(rintangan, 0, -5)  # Geser rintangan ke atas
        canvas.after(i * 50, canvas.move, rintangan, 0, 5)  # Geser kembali ke bawah

# Buat efek skor visual
def tampilkan_efek_skor(x, y):
    """Efek partikel berwarna saat skor bertambah."""
    for i in range(20):
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        efek_id = canvas.create_oval(x + x_offset, y + y_offset, x + x_offset + 2, y + y_offset + 2, fill="green")
        canvas.after(i * 30, canvas.delete, efek_id)

# Fungsi gerakan rintangan
def gerak_rintangan():
    """Menggerakkan rintangan secara terus-menerus."""
    canvas.move(rintangan, 0, 5)  # Geser rintangan ke bawah
    if canvas.coords(rintangan)[3] > 400:  # Jika rintangan keluar layar
        canvas.coords(rintangan, random.randint(50, 350), 0, random.randint(100, 200), 30)  # Reset posisi
        efek_rintangan_melompat()
        tambah_skor()  # Tambah skor jika berhasil menghindari rintangan
    # Periksa tabrakan dengan bola
    if cek_tabrakan():
        x_tabrak = (canvas.coords(bola)[0] + canvas.coords(bola)[2]) // 2
        y_tabrak = (canvas.coords(bola)[1] + canvas.coords(bola)[3]) // 2
        efek_gelombang(x_tabrak, y_tabrak)
        game_berakhir()
    else:
        root.after(50, gerak_rintangan)  # Ulang gerakan setiap 50 milidetik

# Periksa apakah bola bertabrakan dengan rintangan
def cek_tabrakan():
    """Memeriksa apakah bola bertabrakan dengan rintangan."""
    bola_coords = canvas.coords(bola)  # Koordinat bola
    rintangan_coords = canvas.coords(rintangan)  # Koordinat rintangan
    return (
        bola_coords[2] >= rintangan_coords[0] and
        bola_coords[0] <= rintangan_coords[2] and
        bola_coords[3] >= rintangan_coords[1] and
        bola_coords[1] <= rintangan_coords[3]
    )

# Tambahkan skor dan perbarui tampilan
def tambah_skor():
    """Menambah skor dan memperbarui tampilan."""
    global skor
    skor += 1
    update_skornya()
    tampilkan_efek_skor(200, 100)  # Tampilkan efek partikel

# Perbarui skor yang ditampilkan di layar
def update_skornya():
    """Memperbarui teks skor di layar."""
    canvas.delete("skor")
    canvas.create_text(50, 10, text=f"Skor: {skor}", font=("Helvetica", 14, "bold"), fill="blue", tags="skor")

# Fungsi ketika permainan berakhir
def game_berakhir():
    """Menghentikan permainan dan menampilkan pesan akhir."""
    canvas.create_text(200, 200, text="Game Berakhir!", font=("Helvetica", 20), fill="red")
    root.unbind("<Left>")
    root.unbind("<Right>")

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Bola Menghindari Rintangan dengan Efek Visual")

# Kanvas untuk area permainan
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Buat bola
bola = canvas.create_oval(190, 350, 210, 370, fill="blue")  # Bola di posisi awal

# Buat rintangan
rintangan = canvas.create_rectangle(random.randint(50, 350), 0, random.randint(100, 200), 30, fill="red")

# Tambahkan kontrol gerakan menggunakan keyboard
root.bind("<Left>", gerak_kiri)  # Gerak ke kiri
root.bind("<Right>", gerak_kanan)  # Gerak ke kanan

# Mulai animasi rintangan
update_skornya()
gerak_rintangan()

# Jalankan aplikasi
root.mainloop()

