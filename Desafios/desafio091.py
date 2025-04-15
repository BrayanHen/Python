from random import randint
from time import sleep
from operator import itemgetter

ranking=list()

jogadas={ 'jogador1':randint(1,6),
          'jogador2':randint(1,6),
          'jogador3':randint(1,6),
          'jogador4':randint(1,6)}

print('Valores sorteados:')

for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.75)

print('-='*20)
print(f'{'  == RANKING DOS JOGADORES =='}')

ranking = sorted(jogadas.items(), key=itemgetter(1),reverse=True)

for p,j in enumerate(ranking):
    print(f'{p+1}° lugar:{j[0]} com {j[1]} no dado.')


