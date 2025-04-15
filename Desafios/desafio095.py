l = list()

while True:
    d = dict()
    lgol = list()
    total = 0

    d['nome'] = input('Nome:')
    partidas = int(input(f'Quantas partidas {d["nome"]} jogou?:'))

    for g in range(partidas):
        num = int(input(f'    Quantos gols na partida {g + 1}?:'))
        lgol.append(num)
        total += num

    d['gols'] = lgol[:]
    d['total'] = total
    l.append(d.copy())

    escolha = input('Quer continuar? [S/N]:').strip().upper()[0]
    if escolha == 'N':
        break

print('-=' * 30)
print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":>7}')
print('-=' * 30)

for i, p in enumerate(l):
    print(f'{i:<5}{p["nome"]:<15}{str(p["gols"]):<20}{p["total"]:>7}')
print('-=' * 30)

while True:
    esc=int(input('Mostrar dados de qual jogador? [999 para parar]:'))
    print('-=' * 30)
    if esc == 999:
        break
    for p,v in enumerate(l[esc]['gols']):
        print(f'no jogo {p+1} fez {v} gols.')