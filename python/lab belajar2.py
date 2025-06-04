#rekursif
# def rekursif(n):
#     if n == 0:
#         return 0
#     else:
#         return n + rekursif(n-1)
    
# n = 1
# print('Hasil Rekursif', rekursif(n))


#Iteratif
# def iteratif(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#     return total

# n=10
# print('Hasil Interatif: ', iteratif(n))

# # Penguklaangan sekuaensial
# def cari(kata, huruf):
#     for index in range(len(kata)):
#         if kata(index) == huruf:
#             return index
#     return -1

# kata = input('masukan kata: ')
# huruf = input('masukan huruf yang dicari: ')
    
# index = cari(kata, huruf)
# if index == -1:
#     print(huruf, 'tidak ditemukan pada', kata)
# else:
#     print(huruf, 'ada pada index', index)

#list

# hewan = ['kontolodon','dragontol', 'mutant', 'python hideung']
# print(hewan)
# print(hewan[0])
# print(hewan[1])
# print(hewan.append('homonculus'))
# print(hewan)
# hewan[0] = 'burung ku hitam'
# print(hewan)
# hewan.clear() 
# print(hewan)

# def tambahHewan(hewan, tambahan):
#     hewan.append(tambahan)
#     return hewan
# def hapusHewan(hewan, hapus):
#     hewan.remove(hapus)
#     return hewan
# def gantihewan(hewan, ganti, index):
#     hewan[index] = ganti
#     return hewan
# def carihewan(hewan,cari):
#     for index in range(len(hewan)):
#         if hewan[index] == cari:
#             return index
#     return -1
# def cekhewan[hewan,cari]:
#     if cari in hewan:
#         print(cari,'ada dalam list')
#     else:
#         print(cari, 'tidak ada dalam list')
# def cetaklist[hewan]:
#     if len(hewan) == 0:
#         print('list kosong')
#     else :
#         for i in range(len(hewan)):
#             print(hewan[i])
# def clearScreen():
#     os.system('cls')

# selesai = False
# hewan   = []

# while not selesai:
#     clearScreen()
#     print('1. Tambah Hewan')
#     print('2. Hapus Hewan')
#     print('3. asd')
#     print('4. asd')
#     print('5. asd')
#     print('6. asd')
#     print('7. asd')

#     pilihan = int(input('Masukan Pilihan : '))
#     if pilihan == 1:
#         tambahan = input('Masukan Hewan yang ditambahkan: ')
#         hewan    = tambahHewan(hewan,tambahan)
#     elif pilihan == 2:
#         hapus = input('Masukan hewan yang dihapus: ')
#         hewan = hapusHewan(hewan, hapus)
         
#     elif pilihan == 3:
#         ganti = input('Masukan hewan yang diganti: ')
#         index = int(input(' Masukan hewan yang dihapus: '))
#         hewan = gantihewan(hewan,ganti,index)
         
#     elif pilihan == 4:
#         cari = input('Masukan hewan yang dicari: ')
#         index = carihewan(hewan, cari)
#         if index ==-1:
#             print(cari, 'tidak ditemukan')
#         else:
#             print(cari,'ada pada index', index)
#     elif pilihan == 5:
#         cari = input('Masukan hewan yang dicari: ')
#         cekhewan(hewan,cari)
#     elif pilihan ==6:
#         cetaklist(hewan)
#     elif pilihan ==7:
#         selesai = True

# set

# dictinary

# umur = int
# data = {
#     'nama'      : 'Ikbar',
#     'umur'      : umur,
#     'pekerjaan' : 'MahaSiswa'
# }
# print(data)    
# print(data['nama'])    
# print(data['umur'])
# print(data['pekerjaan'])

# data['umur'] = 22
# print(data)

# print(data.keys())
# print(data.values())




         