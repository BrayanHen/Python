try:
    a=int(input('Numero:'))
    b=int(input('Numero:'))
    r=a/b
except ZeroDivisionError:
    print(f'\033[31mErro! Divisão por Zero não é uma operação valida.\033[m')
except (ValueError, TypeError):
    print(f'\033[31mErro! Dados invalidos.\033[m')
except KeyboardInterrupt:
    print(f'\033[31mErro! Campo Vazio.\033[m')
except Exception as erro:
    print(f'\033[31mErro: {erro.__cause__}\033[m')
else:
    print(f'{a} / {b} = {r:.2f}')
finally:
    print('\033[32mFim do programa!\033[m')




