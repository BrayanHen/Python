n = int(input('Digite um numero:'))
print('Analisando o Numero {}'.format(n))

uni= n // 1 % 10
dez= n // 10 % 10
cen= n // 100 % 10
mil= n // 1000 % 10
dzm= n // 10000 % 10
ctm= n // 100000 % 10
mlh= n // 1000000 % 10

print('Unidade:{}'.format(uni))
print('Dezena:{}'.format(dez))
print('Centena:{}'.format(cen))
print('Milhar:{}'.format(mil))
print('Dezena  de Milhar:{}'.format(dzm))
print('Centena de Milhar:{}'.format(ctm))
print('Milhão :{}'.format(mlh))
