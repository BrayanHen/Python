from random import randint

bot = randint(1, 10)

print('-=-'*20)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-=-'*20)

tentativa=0
acertou = False
while not acertou:
    palpite=int(input('Qual o seu palpite?:'))
    tentativa += 1
    if palpite==bot:
        acertou = True
        print('Acertou com {} tentativas.'.format(tentativa))
    elif palpite<bot:
        print('Mais... Tente novamente!')
    elif palpite>bot:
        print('Menos... Tente novamente!')



