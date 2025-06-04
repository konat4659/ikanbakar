def hitung_huruf():
    while True:
       
        kalimat = input("Masukkan sebuah kalimat: ")
        kata_kata = kalimat.split()
        print("\nJumlah huruf pada setiap kata:")
        for kata in kata_kata:
            print(f"'{kata}': {len(kata)} huruf")

        coba_lagi = input("\nApakah Anda ingin mencoba lagi? (ya/tidak): ").strip().lower()
        if coba_lagi != "ya":
            print("Terima kasih telah menggunakan program ini!")
            break


hitung_huruf()
