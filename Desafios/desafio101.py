def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos:NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos:VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos:VOTO OBRIGATORIO!'

print('--'*15)
nasc= int(input('Ano de nascimento:'))
print(voto(nasc))