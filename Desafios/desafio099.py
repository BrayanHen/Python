def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
    else:
        for n in num:
            print(n, end=' ', flush=True)
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior valor informado foi {max(num)}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()