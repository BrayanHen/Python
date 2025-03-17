n1=float(input('Digite a primeira nota para calculo da média:'))
n2=float(input('Digite a segunda nota para calculo da média:'))

media=(n1+n2)/2

if media<5:
    print('Reprovado!')
elif media>=5 and media<7:
    print('Recuperação!')
if media>=7:
    print('Aprovado!')