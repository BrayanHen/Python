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

def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mErro! digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro! entrada de dados interrompida.\033[m')
            return 0
        else:
            return num

n1=leiaint('Digite um numero inteiro:')
n2=leiafloat('Digite um numero real:')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2} .')