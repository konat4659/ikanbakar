
nama = input('Masukan nama anda: ')
nim = int(input('Masukan NIM anda: '))


print('''
Masukan 2 buah bilangan''')
angka1 = int(input('''bilangan pertama:'''))
angka2 = int(input('''bilangan kedua:'''))
 

pilihan = int(input('''
 1. perkalian
 2. penjumlahan
 3. pengurangan
 4. pembagian      
 pilih nomor: '''))
if pilihan == 1:
        print('HASIL:', angka1*angka2)
elif pilihan == 2:
        print('HASIL:', angka1+angka2)
elif pilihan == 3:
        print('HASIL:', angka1-angka2)
elif pilihan == 4:
        print('HASIL:', angka1/angka2)




