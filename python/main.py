# import os
# def create_file():
#     try:
#         namafile = input('Masukkan nama file: ')
#         file = open(namafile, 'x')
#         file.close()
#         print('File created')
#     except FileExistsError:
#         print("File already exists")

# def read_file():
#     try:
#         namafile = input('Masukkan nama file: ')
#         file = open(namafile, 'r')
#         print(file.read())
#         file.close()
#     except FileNotFoundError:
#         print('file not found')

# def update_file():
#     try:
#         file = open('data.txt', 'a')
#         tulisan = int(input('masukan berapa kali data akan ditambahkan: '))
#         for i in range(tulisan):
#             data = input(f'line ke-{i+1}:')
#             file.write(data + '\n')
#         file.close()
#         print('data added')
#     except FileNotFoundError:
#         print('file not found')

# def delete_file():
#     try:
#         os.remove('data.txt')
#         print('File Deleted')
#     except FileNotFoundError:
#         print("File not found")

# def main():
#     while True:
#         print('masukan file txt')
#         print('1. creat file')
#         print('2. read file')
#         print('3.update file')
#         print('4. delete file')
#         print('masukan file txt')
#         pilihan = input('masukan pilihanmu: ')

#         if pilihan == '1':
#             create_file()
#         elif pilihan == '2':
#             read_file()
#         elif pilihan == '3':
#             update_file()
#         elif pilihan == '4':
#             delete_file()
#         elif pilihan == '5':
#             break
#         else:
#             print('pilihan tidak valid')
#         input('press enter to continue...' )
#         os.system('cls')


# main()




import sqlite3
import os
def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()


    query = '''
    '''

    cursor.execute(query)
    conn.commit()
    conn.close()


def insert_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    nim = input( 'nim' )

def insert_data():
    query = ()

    
    