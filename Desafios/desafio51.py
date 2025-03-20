print(f'{'=='*20:^40}')
print(f'{'10 TERMOS DE UMA PA':^40}')
print(f'{'=='*20:^40}')

termo=int(input('Primeiro termo:'))
razao=int(input('Razão:'))
an= termo + (11-1) * razao

for c in range(termo,an,razao):
    print(c,''' → ''', end='')
print(' FIM')

#descobrir ultimo termo da PA:termo + (11-1) * razao




