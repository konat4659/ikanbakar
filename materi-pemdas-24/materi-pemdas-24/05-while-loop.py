# Contoh while loop
angkaRahasia = 7
gameTerusBerjalan = True
while gameTerusBerjalan:
    tebakanPeserta = int(input("Masukkan Tebakan anda: "))

    if (tebakanPeserta == angkaRahasia):
        print("Tebakan anda benar, selesai!")
        gameTerusBerjalan = False
    else:
        print("Tebakan anda salah!")
