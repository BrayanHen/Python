def area(l,c):
    area=l*c
    print(f'A área de um terreno {l}x{c} é de {area}m²')


print(f'{'Controle de Terrenos':^20}')
print('-'*21)
l=float(input('LARGURA (m):'))
c=float(input('COMPRIMENTO (m):'))
area(l,c)