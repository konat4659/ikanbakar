print('***TUGAS PROGRAMING***')

nama_pengguna = (input('Masukan Nama Mu:'))
umur = int(input('berapa umurmu:'))
tinggi = float(input('berapa tinggi mu:'))

print(f'Nama {nama_pengguna}')
print(f'umur {umur}')
print(f'tinggi {tinggi}')

print(f'''
      

                         Halo {nama_pengguna}!!
      Di bawah ini ada beberapa quiz yang harus anda selesaikan
                       Selamat mengerjakan
     
      pilih (a,b,c) untuk menjawab!!! ''')

Nilai = 0


#pertanyaan 1
pertanyaan_1 = (input("""
    1.Siapa presiden pertama indonesia?
                      
    a.Soekarno
    b.Sutono
    c.Subarjo
    
    jawab:"""))
jawaban_1 = 'a'

print(f'''{pertanyaan_1}''')

if pertanyaan_1 == jawaban_1:
    Nilai = Nilai + 10
    print(f'Jawaban Anda Benar, Nilai Anda menjadi {Nilai}')
else:
    Nilai = Nilai + 0
    print(f'Jawaban Anda Salah, Nilai Anda menjadi {Nilai}')

#pertanyaan 2
pertanyaan_2 = (input("""
    2.Berapa hasil dari 11x11?
    
    a.131
    b.145
    c.121    
                                   
    Jawab:"""))
jawaban_2 = 'c'

print(pertanyaan_2)

if pertanyaan_2 == jawaban_2:
    Nilai = Nilai + 10
    print(f'Jawaban Anda Benar, Nilai anda menjadi {Nilai}')
else:
    Nilai = Nilai + 0
    print(f'Jawaban Anda Salah, Nilai anda menjadi {Nilai}')

#pertanyaan 3
pertanyaan_3 = (input("""
    Berapa nilai dari π?
                      
    a.3,78
    b.3,16
    c.3,14
    jawab:""")) 
jawaban_3 = 'c'

print(pertanyaan_3)

if pertanyaan_3 == jawaban_3:
    Nilai = Nilai + 10
    print(f'Jawaban Anda Benar, Nilai anda menjadi {Nilai}')
else:
    Nilai = Nilai + 0
    print(f'Jawaban Anda Salah, Nilai anda menjadi {Nilai}')
   
print(f'''
      
      
      Selamat anda telah menyelesaikan pertanyaan dengan total nilai {Nilai}''')