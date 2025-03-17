from datetime import date
ano=int(input('Digite o ano de nascimento para analise:'))

idade=date.today().year - ano
tp=18-idade
tp2=idade-18

if idade<18:

     print('Ainda vai se alistar no serviço militar')

     print('Falta {} ano(s) para voce se alistar'.format(tp))

elif idade == 18:

    print('Hora de se alistar!')

elif idade>18:

    print('Passou da hora de se alistar!')

    print('Já passou {} ano(s) do prazo do seu alistamento'.format(tp2))

print('Obrigrado pelo seus serviços soldado!')


