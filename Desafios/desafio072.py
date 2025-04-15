import num2words
num=int(input('Digite um numero[entre 1 e 20]:'))
if num >= 1 and num <= 20:
    print(f'Você digitou o numero {num2words.num2words(num,lang='pt')}.')
else:
    print('Numero inválido! Digite um numero entre 1 e 20')
