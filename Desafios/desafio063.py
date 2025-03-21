print('---'*12)
print(f'{'Sequencia de Fibonacci':^35}')
print('---'*12)
termos=int(input('Quantos termos você quer mostrar?:'))
t1=0
t2=1
print('~~~'*12)
print('{} -> {}'.format(t1,t2),end='')
cont=3
while cont <= termos:
    t3=t1+t2
    print('-> {}'.format(t3),end='')
    t1=t2
    t2=t3
    cont+=1
print('  Fim')
print('~~~'*12)