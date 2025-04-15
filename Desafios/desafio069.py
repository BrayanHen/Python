maior=0
M=0
F=0
while True:
    print('--'*15)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('--' * 15)
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [M/F]:')).upper()[0]
    print('--'*15)
    escolha=str(input('Quer continuar? [S/N]:')).upper()[0]
    if idade >= 18:
        maior+=1
    if sexo == 'M':
        M+=1
    if sexo == 'F' and idade < 20:
        F+=1
    if escolha=='N':
        print(f'Total de pessoas maiores de idade: {maior}')
        print(f'Ao todo temos {M} homens cadastrados.')
        print(f'E temos {F} mulheres com menos de 20 anos.')
        break