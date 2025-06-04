def input_data():
    nama = input('Masukan Nama Anda: ')
    nim = int(input('Masukan Nim Anda: '))
    print('Halo:', nama, nim)

    print ('Masukan Pilihan anda')

def kalkulator_io():
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')


    operasi = int(input('Masukan pilihan 1-4: '))

    angka1 = float(input('Masukan angka pertama: '))
    angka2 = float(input('Masukan angka kedua: '))

    if operasi == 1:
        hasil = angka1 + angka2
        operasi_str = "Penjumlahan"
    elif operasi== 2:
        hasil = angka1 - angka2
        operasi_str: "Pengurangan"
    elif operasi== 3:
        hasil = angka1 * angka2
        operasi_str: "Perkalian"
    elif operasi== 4:
        hasil = angka1 / angka2
        operasi_str: "Pembagian"
        if 
def menu():
    while True: