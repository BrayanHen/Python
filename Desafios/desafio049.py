num=int(input('Digite um numero para ver sua tabuada:'))
for t in range(1,11):
    multi = num * t
    print('{} x {:2} = {}'.format(num,t,multi))

