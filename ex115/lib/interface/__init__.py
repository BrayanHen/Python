def linha(size= 42):
    return '-' * size

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont=1
    for item in lista:
        print(f'\033[33m{cont}\033[m. \033[35m{item}\033[m')
        cont+=1
    print(linha())
    opc=leiaint('\033[33mSua opção:\033[m')
    return opc

def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mErro! digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro! entrada de dados interrompida.\033[m')
            return 0
        else:
            return num