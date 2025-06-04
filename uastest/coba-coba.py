import random

pemain = input('pilih kertas,gunting,batu:')
print('pemain:', pemain)
game = ['kertas','gunting','batu']
randompik = random.randrange(0,len(game))
print('bot:', game[randompik])