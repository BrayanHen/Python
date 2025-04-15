cont = 0
lista = []
maior = None
menor = None
nomes_maior = []
nomes_menor = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    lista.append([nome, peso])
    cont += 1

    if maior is None or peso > maior:
        maior = peso
        nomes_maior = [nome]
    elif peso == maior:
        nomes_maior.append(nome)

    if menor is None or peso < menor:
        menor = peso
        nomes_menor = [nome]
    elif peso == menor:
        nomes_menor.append(nome)

    escolha = input("Quer continuar? [S/N]: ").strip().upper()
    if escolha == "N":
        break


print(f'\nAo todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi {maior} kg. Peso de {", ".join(nomes_maior)}.')
print(f'O menor peso foi {menor} kg. Peso de {", ".join(nomes_menor)}.')