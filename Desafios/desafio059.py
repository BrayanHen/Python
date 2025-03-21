n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
r=True
while r:
    print('      [1] somar\n      [2] multiplicar\n      [3] maior\n      [4] novos números\n      [5] sair do programa')
    opcao = input('>>>>>Qual sua opção?:')

    soma = n1 + n2
    mult = n1 * n2
    maximo = max(n1, n2)

    if opcao not in '12345':
        print('Opção invalida.Por favor digite uma opção valida')
        print('=-=' * 10)

    if opcao=='1':
        print('A soma soma entre {} + {} é {} '.format(n1,n2,soma))
        print('=-=' * 10)

    if opcao=='2':
        print('O resultado de {} x {} é {} '.format(n1,n2,mult))
        print('=-=' * 10)

    if n1==n2 and opcao=='3':
        print('Os numeros são iguais.Então não tem um maior!')
        print('=-=' * 10)
    else:
        if opcao == '3':
            print('O maior valor entre {} e {} é {} '.format(n1,n2,maximo))
            print('=-=' * 10)
    if opcao=='4':
        print('Digite os numeros novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    if opcao=='5':
        r=False

print('Fim do programa')

