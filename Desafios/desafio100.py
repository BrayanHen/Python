from random import randint
def sorteia():
    sort = []
    print('Sorteando 5 valores da lista:', end=' ', flush=True)
    for c in range(0, 5):
        rand=randint(1,10)
        print(rand, end='  ', flush=True)
        sort.append(rand)
    print('PRONTO!')
    return sort

def somaPar():
    lista = sorteia()
    contador = 0
    print(f'Somando os valores pares de {lista} temos:',end=' ')
    for n in lista:
        if n % 2 == 0:
            contador += n
    print(contador)
somaPar()


