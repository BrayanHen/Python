d=int(input('Quantos dias alugados?:'))
km=float(input('Quantos Km rodados?:'))
da=60*d
ks=0.15*km
r=da+ks

print('O total a pagar é de R$:{:.2f}'.format(r))