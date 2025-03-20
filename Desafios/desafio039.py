from datetime import date
ano=int(input('Digite o ano de nascimento para analise:'))

idade=date.today().year - ano
tempo_que_falta=18-idade
tempo_que_passou=idade-18
ano_atual=date.today().year

if idade<18:
     print('Ainda vai se alistar no serviço militar')
     print('Falta {} ano(s) para voce se alistar'.format(tempo_que_falta))
     print('Voce ira se alistar em:{}'.format(ano_atual+tempo_que_falta))
elif idade == 18:
    print('Hora de se alistar!')
elif idade>18:
    print('Passou da hora de se alistar!')
    print('Já passou {} ano(s) do prazo do seu alistamento'.format(tempo_que_passou))
    print('O seu alistamento foi em:{}'.format(ano_atual-tempo_que_passou))
print('Obrigrado pelo seus serviços soldado!')


