from ex109 import moeda

num=float(input('Digite o preço:R$'))
print(f'A metade {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num,10,True)}')