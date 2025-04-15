from random import randint
print('=-'*15)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^28}')
print('=-'*15)
cont=0
computador = randint(1, 10)

while True:
    jogador = int(input('Digite um valor:'))
    escolha = str(input('Par ou Impar? [P/I]:')).upper()[0]
    print('--' * 15)
    soma = computador + jogador
    print(f'Você jogou {jogador} e o computador {computador}.Total de {soma}',end=' ')

    if soma % 2 == 0:
        print('DEU PAR!')
        print('--' * 15)
    else:
        print('DEU IMPAR!')
        print('--' * 15)

    if jogador % 2 == 0 and soma % 2 == 0:
        print('Você GANHOU!... Vamos jogar novamente!')
        cont+=1
        print('-='*15)
    if jogador % 2 == 1 and soma % 2 == 1:
        print('Você GANHOU!... Vamos jogar novamente!')
        cont+=1
        print('-=' * 15)
    if jogador % 2 == 0 and soma % 2 == 1 or jogador % 2 == 1 and soma % 2 == 0:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Você venceu {cont} vezes!')
        break


