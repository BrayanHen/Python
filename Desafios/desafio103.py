def ficha(jogador='<Desconhecido',gols=0):
    return f'O jogador {jogador} fez {gols} gols.'

j=(input('Nome do jogador:')).strip()
g=input('Numero de gols:').strip()

if g.isnumeric():
    g=int(g)
else:
    g=0

if j=='':
    j='<Desconhecido>'

print(ficha(j,g))