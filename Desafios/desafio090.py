aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] =float(input(f'Média de {aluno["nome"]}:'))
print('-='*15)
print('Nome:', aluno['nome'])
print('Média:', aluno['média'])
if aluno['média'] <7:
    aluno['situação']= 'Recuperação'
if aluno['média']>=7:
    aluno['situação']= 'Aprovado'
print('Situação:',aluno['situação'])
