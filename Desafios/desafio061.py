print(f'{'Gerador de PA':^40}')
print(f'{'-=-'*15:^40}')

termo=int(input('Primeiro termo:'))
razao=int(input('Razão:'))

for c in range (termo,razao*10,razao):
    print(c,'➞' if c<razao*10 else 'Fim',end=' ')
print('Fim',end=' ')