from math import factorial
num=int(input('Digite um numero para calcular seu Fatorial:'))
print('Calculando {}! = '.format(num),end='')
c=num
while c>0:
  print('{}'.format(c),end='')
  print(' x ' if c>1 else ' = ',end='')
  c -= 1
print('{}'.format(factorial(num)))





