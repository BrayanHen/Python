def ajuda(com):
    help(com)

while True:
    print('\033[0;35m~~\033[m' * 20)
    print(f'{'\033[0;35mSistema de Ajuda PYHELP\033[m':^50}')
    print('\033[0;35m~~\033[m' * 20)

    f=input('Função da biblioteca:')

    if f == 'fim':
        print('\033[0;31m~~\033[m' *6)
        print(f'{'\033[0;31m ATÉ LOGO!\033[m':^15}')
        print('\033[0;31m~~\033[m' * 6)
        break

    print('\033[0;33m~~\033[m'*20)
    print(f'\033[0;33mAcessando o manual do comando {f}\033[m')
    print('\033[0;33m~~\033[m' * 20)

    ajuda(f)
