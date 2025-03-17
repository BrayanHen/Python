import random
import time
print('Vamos jogar Pedra, Papel ou Tesoura!')
time.sleep(1.5)
jogador=(input('Escolha entre Pedra Papel ou Tesoura:')).upper()

lista=['PEDRA','PAPEL','TESOURA']
bot=random.choice(['PEDRA','PAPEL','TESOURA'])
#empate
if jogador=='PEDRA' and bot=='PEDRA':
    print('Empate!')
elif jogador=='PAPEL' and bot=='PAPEL':
    print('Empate!')
elif jogador=='TESOURA' and bot=='TESOURA':
    print('Empate!')
#jogador ganha
if jogador=='PEDRA' and bot=='TESOURA':
    print('Voce Ganhou! eu escolhi Tesoura.')
elif jogador=='PAPEL' and bot=='PEDRA':
    print('Voce Ganhou! eu escolhi Pedra.')
elif jogador=='TESOURA' and bot=='PAPEL':
    print('Voce Ganhou! eu escolhi Papel.')
#bot ganha
if jogador=='PAPEL' and bot=='TESOURA':
    print('Eu ganhei! eu eu escolhi Tesoura.')
elif jogador=='TESOURA' and bot=='PEDRA':
    print('Eu ganhei! eu eu escolhi Pedra.')
elif jogador=='PEDRA' and bot=='PAPEL':
    print('Eu ganhei! eu eu escolhi Papel.')

