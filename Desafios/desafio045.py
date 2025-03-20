import random
import time
print('Vamos jogar Pedra, Papel ou Tesoura!')
time.sleep(.75)

jogador=(input('Escolha entre Pedra Papel ou Tesoura:')).upper()
lista=['PEDRA','PAPEL','TESOURA']
bot=random.choice(['PEDRA','PAPEL','TESOURA'])

print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PO!!!')

#empate
if jogador=='PEDRA' and bot=='PEDRA':
    print('Empate!Eu tambem escolhi {}'.format('PEDRA'))
elif jogador=='PAPEL' and bot=='PAPEL':
    print('Empate!Eu tambem escolhi {}'.format('PAPEL'))
elif jogador=='TESOURA' and bot=='TESOURA':
    print('Empate!Eu tambem escolhi {}'.format('TESOURA'))
#jogador ganha
if jogador=='PEDRA' and bot=='TESOURA':
    print('Voce Ganhou! eu escolhi Tesoura.')
elif jogador=='PAPEL' and bot=='PEDRA':
    print('Voce Ganhou! eu escolhi Pedra.')
elif jogador=='TESOURA' and bot=='PAPEL':
    print('Voce Ganhou! eu escolhi Papel.')
#bot ganha
if jogador=='PAPEL' and bot=='TESOURA':
    print('Eu ganhei! eu  escolhi Tesoura.')
elif jogador=='TESOURA' and bot=='PEDRA':
    print('Eu ganhei! eu  escolhi Pedra.')
elif jogador=='PEDRA' and bot=='PAPEL':
    print('Eu ganhei! eu  escolhi Papel.')
