import random

print('Pensando...')
print('Descubra o numero entre 0 e 5 que eu pensei!')
n=int(input('Adivinhe o numero q eu pensei!: '))
p=random.randint(0,5)

if n == p:
    print('Voce acertou')
else:
    print('Voce errou')

print('O numero que eu pensei foi:{}'.format(p))

