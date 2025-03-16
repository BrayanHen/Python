l1=int(input('Digite um numero:'))
l2=int(input('Digite um numero:'))
l3=int(input('Digite um numero:'))
l4=int(input('Digite um numero:'))
l5=int(input('Digite um numero:'))

r=(l1,l2,l3,l4,l5)
mv=max(r)
mnv=min(r)
pos=r.index(mv)+1
posm=r.index(mnv)+1

print(r)
print('Maior:{} (posição {})'.format(mv,pos))
print('Menor Valor:{} (posição {})'.format(mnv,posm))
