def resumo(a,b,c):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'{'Preço analisado: R$':<15}{a:>11}')
    print(f'{'Dobro do preço: R$':<15}{a*2:>12}')
    print(f'Metade do preço: R${a/2:<12}')
    aumento=a*b/100
    print(f'{b}% de aumento: R${a+aumento:<12}')
    diminuindo=a*c/100
    print(f'{c}% de aumento: R${a-diminuindo:<12}')
    print('-'*30)