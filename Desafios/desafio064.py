num=0
soma=0
r=0
while r != 999:
    r = int(input('Digite um numero [999 para parar]:'))
    soma += r
    num += 1
    if r==999:
         print('Voce digitou {} números e a soma entre eles foi {}'.format(num-1,soma-999))