r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento'))

if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('Esses segmentos  podem formar um triangulo')

    if r1 == r2 and r2 == r3 and r3 == r1:
        print('Triangulo Equilatero')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')


else:
    print('Esses segmentos não podem formar um triangulo')





# valor um != valor 2 =valor um diferente de valor 2 (so considera oq tiver entre os operadores !=
