num=int(input('Digite um numero:'))
escolha=input('Quer continuar? [S/N]:').strip().upper()[0]

cont = 1
soma=num
maior=num
menor=num

while escolha == 'S':
    num=int(input('Digite um numero:'))
    escolha=input('Quer continuar? [S/N]:').strip().upper()[0]

    soma+=num
    cont += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / cont

print('Voce digitou {} numeros e a media foi {} '.format(cont,media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))