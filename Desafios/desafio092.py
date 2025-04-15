from datetime import datetime

trabalhador= {}

trabalhador['nome']=input('Nome:')
nasc=int(input('Ano de nascimento:'))
idade=datetime.today().year - nasc
trabalhador['carteira de trabalho']= int(input('Carteira de Trabalho [0 não tem]:'))

if trabalhador['carteira de trabalho']!=0:
    trabalhador['ano de contratação']=int(input('Ano de contratação:'))
    trabalhador['salario']=float(input('Salario:'))

print('-='*30)
apos=idade+30

print('- Nome:',trabalhador['nome'])
print(f'- idade:{idade}')

if trabalhador['carteira de trabalho']==0:
    print('- Carteira de trabalho: Não tem carteira de trabalho.')

if trabalhador['carteira de trabalho']!=0:
    print('- Carteira de trabalho:',trabalhador['carteira de trabalho'])

    print('- Ano de contratação:',trabalhador['ano de contratação'])

    print('- Salario:',trabalhador['salario'])

    print(f'- Aposentadoria:{apos}')