def metade(num,formato=False):
    res=num/2
    return res if formato is False else moeda(res)

def dobro(num,formato=False):
    res=num*2
    return res if formato is False else moeda(res)

def aumentar(num,taxa, formato=False):
    res=num+(num*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(num,taxa, formato=False):
    res=num-(num*taxa/100)
    return res if formato is False else moeda(res)

def moeda(num):
    return f'R${num:.2f}'.replace('.',',')

def resumo(p,a,d):
    print('-'*32)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 32)
    print(f'{'Preço analisado:':<20}  {moeda(p):}')
    print(f'{'Dobro do preço:':<19}   {dobro(p,True)}')
    print(f'{'Metade do preço:':<20}  {metade(p,True)}')
    print(f'{f'{a}% de aumento:':<20}  {aumentar(p,a,True)}')
    print(f'{f'{d}% de redução:':<20}  {diminuir(p,d,True)}')
    print('-'*32)