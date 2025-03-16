v=float(input('Qual o tamanho da viagem em km/h:'))

val=v*0.50
val2=v*0.45

if v <= 200:
    print('O valor da viagem é:{}'.format(val))
else:
    print('O valor da viagem é:{}'.format(val2))