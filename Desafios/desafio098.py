from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ', flush=True)
            sleep(0.3)
    else:
        for c in range(i, f - 1, -p):
            print(c, end=' ', flush=True)
            sleep(0.3)
    print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i=int(input('Inicio:'))
f=int(input('Fim:'))
p=int(input('Passo:'))
contador(i, f, p)