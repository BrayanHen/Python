dict={}
cont=0
lista=list()
dict['nome']=str(input('Nome do jogador:'))
partidas=int(input(f'Quantas partidas {dict['nome']} jogou?:'))
for c in range(0,partidas):
     num=int(input(f'Gols na partida {c+1}:'))
     cont+=num
     lista.append(num)
     dict['gols']=lista
     dict['total']=cont
print('-='*30)
print(dict)
print('-='*30)
for k,v in dict.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dict['nome']} jogou {partidas} partidas.')
for c in range(0,partidas):
    print(f'     => Na partida {c+1}, fez {lista[c]} gols.')
print(f'Foi um total de {cont} gols.')