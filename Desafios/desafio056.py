med=0
maior=0
mulher=0
for c in range(1, 5):
    print('-----{}ᵃ PESSOA-----'.format(c))

    nome=input('Nome:')
    idade=int(input('Idade:'))
    sexo=input('Sexo [M/F]:').upper()

    med += idade
    media=med/4

    if sexo=='M' and  c==1:
        maior=idade
    else:
        if idade>maior:
            maior=idade
            nm: str=nome
    if sexo=='F' and idade<20:
        mulher+=1

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nm))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))