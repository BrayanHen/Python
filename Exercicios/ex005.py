from num2words import num2words

n=int(input('Digite um numero entre 0 e 20:'))

r=num2words(n, lang='pt').capitalize()

print('Voce digitou o número:{}'.format(r))