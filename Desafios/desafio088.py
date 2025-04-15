import random
from time import sleep
print('--'*20)
print(f'{'JOGUE NA MEGA SENA':^40}')
print('--'*20)
jogos=int(input('Quantos jogos você quer q eu sorteie?:'))
print(F'-=-=-=  SORTEANDO {jogos} JOGOS  =-=-=-=-=')
for jogo in range(0,jogos):
    rand = random.sample(range(1, 60), 6)
    print(f'Jogo {jogo + 1}:{rand}\n', end='')
    sleep(.75)
print('-=-=-=-=-=-= < BOA SORTE! >-=-=-=-=-=')