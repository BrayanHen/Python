import calendar

ano=int(input('Digite um ano para saber se ele é bissexto:'))

r=calendar.isleap(ano)

if r == True:
     print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')


#se o ano for bissexto isleap retorna True se não retorna False