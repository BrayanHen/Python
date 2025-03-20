n=int(input('Digite um numero:'))
total=0
for i in range(1,n+1):
    if n % i ==0:
        print('\033[33m',end='')
        total=total+1
    else:
        print('\033[31m', end='')
    print('{} '.format(i),end='')
if total==2:
    print('\n\033[m{} É primo'.format(n))
else:
    print('\n\033[m{} Não é primo'.format(n))



