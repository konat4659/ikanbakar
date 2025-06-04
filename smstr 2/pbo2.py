class Ortu:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def infokan(self):
        print(f'Nama: {self.nama}\numur: {self.umur}\n')
class Anak(Ortu):
    def __init__(self, hobi):
        self.hobi = hobi
    def infoAnaknya(self,SelisihUmurAnak):
        print(f'Nama: {self.nama}\numur: {self.umur - SelisihUmurAnak}\nHobi: {self.hobi}')

bapak = Ortu('Ujang',43)
bapak.infokan()
anak = Anak('BELAJAR')
anak.nama = 'satir'
anak.umur = 43
anak.infoAnaknya(23)

        