print(f'{'Gerador de PA':^40}')
print(f'{'-=-'*15:^40}')

termo=int(input('Primeiro termo:'))
razao=int(input('Razão:'))

for c in range (termo,razao*10,razao):
    print(c,'➞' if c<razao*10 else 'Fim',end=' ')
print('PAUSA')
termo_mais = int(input('Quantos termos você quer mostrar a mais?:'))
for c in range (razao*10,razao*10*termo_mais,razao):
    print(c)
    if termo_mais == 0:
        print('Progressão finalizada com {} termos mostrados'.format(10 + (termo_mais)))
print('Progressão finalizada com {} termos mostrados'.format(10 + (termo_mais)))
