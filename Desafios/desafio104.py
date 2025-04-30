def leiaInt(txt):
    while True:
        num=input(txt)
        if num.isnumeric():
            print(f'Voce digitou o numero {int(num)}')
            break
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido \033[m')
            print(f'\033[31mErro! Digite um numero inteiro válido.\033[m')
leiaInt('Digite um numero:')
