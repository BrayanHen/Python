cdt=dict()
lista=list()
c=0
while True:
    cdt['nome']=str(input('Nome:'))

    while True:
        sexo=str(input('Sexo[M/F]:')).upper()[0]
        if sexo in 'MF':
            cdt['sexo']=sexo
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    cdt['idade']=int(input('Idade:'))
    c+=cdt['idade']
    lista.append(cdt.copy())

    while True:
        escolha=str(input('Quer continuar?[S/N]:')).upper()[0]
        if escolha in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')

    if escolha == 'N':
            break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
media=c/len(lista)
print(f'A média de idade é de {media:.2f} anos')
print('Lista das pessoas acima da média:')
for p in lista:
    if p['idade'] > media:
        print(f'nome = {p["nome"]}; sexo = {p['sexo']} idade = {p["idade"]}')