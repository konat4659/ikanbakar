

# untuk membersihkan program yang berjalan sebelumnya
import os
os.system('cls')

# spasi
def echo():
    print('')
    
# meminta 2 bilangan yang akan dibagi    
def reqNum():
    while True:
        try:
            num = float(input(f'Masukan bilangan: '))
            return num
        except ZeroDivisionError: # jika input angka 0, maka akan mendapat notice diminta memasukan angka selain 0
            print('MASUKAN BILANGAN SELAIN 0!')
        except ValueError: # jika input bukan angka, maka akan mendapat notice dan akan diminta memasukan angka
            print('Masukan bilangan yang benar!')
            

# fungsi proses pembagain 2 bilangan yang dimasukan            
def proses(num1,num2):
    try:
        eq = num1 / num2
        print(f'Hasil dari {num1} : {num2} adalah {eq}')
    except ZeroDivisionError:
        print('MASUKAN BILANGAN SELAIN 0!')

def main():
    while True:
        print('===== Pembagian =====')
        echo()
        
        try:
            num1 = reqNum()
            num2 = reqNum()
            echo()
        except ZeroDivisionError:
            print('MASUKAN BILANGAN SELAIN 0!')
        proses(num1, num2)
        echo()
        echo()
    
main()
