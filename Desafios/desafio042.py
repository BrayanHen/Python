r1=float(input('Digite o tamanho da primeira reta:'))
r2=float(input('Digite o tamanho da segunda reta:'))
r3=float(input('Digite o tamanho da terceira reta:'))

if r1+r2 > r3:
    print('Esses segmentos de reta podem formar um triangulo')
if r1 == r2 and r2==r3 and r3==r1:
    print('Triangulo Equilatero')
elif r1 ==r2 or r1 == r3 or r2==r3 or r3==r1:
    print('Triangulo Isosceles')
else:
    print('Escaleno')


