from math import floor
s=int(input('Salario do funcionario:'))
s10=s*10/100
s15=s*15/100

if s > 1250 :
    print('O aumento será de:{:.2f}'.format(s10))
else:
    print('O aumento será de {:.2f}'.format(s15))