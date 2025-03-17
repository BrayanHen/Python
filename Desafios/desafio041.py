import datetime
ano=int(input('Digite o ano de nascimento do atleta:'))

idade=datetime.date.today().year - ano


if idade<= 9:
    print('MIRIM')
elif idade>9 and idade<= 14:
    print('INFANTIL')
elif idade>14 and idade<=19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
else:
    print('MASTER')

