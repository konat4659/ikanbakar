#counter = 0

#while True:

gameangka = 6
loop = True
# perubahan
while True:
    tebakanpemain = int(input('masukan tebakan anda: '))

    if (tebakanpemain == gameangka):
        print("tebqakan anda benar")
        loop = False
    else:
        print('tebakan salah')

