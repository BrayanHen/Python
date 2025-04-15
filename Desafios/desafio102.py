def fatorial(numero,show=False):
    '''
    -> Calcula o fatorial de um numero
    :param numero: O numero a ser calculado
    :param show:(opcional) Mostra ou não o calculo
    :return:O valor do fatorial de um numero n.
    '''
    f=1
    if show:
        for c in range(numero,0,-1):
            print(c,end=' x ' if c > 1 else ' = ')
            f*=c
    else:
        for c in range(numero,0,-1):
            f*=c
    print(f,end=' ')

fatorial(5,show=True)