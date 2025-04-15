while True:
    print('-'*30)
    num=int(input('Quer ver a tabuada de qual valor?:'))
    print('-'*30)
    if num>0:
        for n in range(1, 11):
            print(f'{num} x {n} = {num * n}')
    else:
        print('Fim do programa!')
        break




