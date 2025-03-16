v=float(input('Qual a velocidade do carro em km/h?:'))
multa=(v-80)*7

if v <= 80:
    print('Esse carro não será multado.')
else:
    print('Esse carro será multado.')
    print('E a multa vai custar {} reais'.format(multa))

print('Tenha um bom dia!')

n1=int(input('digite um valor'))
