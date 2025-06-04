# untuk membersihkan program yang berjalan sebelumnya
import os
os.system('cls')
    
# meminta 2 bilangan yang akan dibagi    
def Except0(num1, num2):
    try:
        eq = num1 / num2
    except ZeroDivisionError: # jika input angka 0, maka akan mendapat notice diminta memasukan angka selain 0
        print('MASUKAN BILANGAN SELAIN 0!')
    except ValueError: # jika input bukan angka, maka akan mendapat notice dan akan diminta memasukan angka
        print('Masukan bilangan yang benar!')
            
# fungsi proses pembagain 2 bilangan yang dimasukan            
def ExceptionNotNum():
    try:
        eq = num1 / num2
        print(f'Hasil dari {num1} : {num2} adalah {eq}')
    except ZeroDivisionError:
        print('MASUKAN BILANGAN SELAIN 0!')

print('===== Pembagian =====')

try:
    num1 =
    num2 = reqNum2()
    
except ZeroDivisionError:
    print('MASUKAN BILANGAN SELAIN 0!')
proses(num1, num2)