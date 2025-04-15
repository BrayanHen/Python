# Desafio 71 - Caixa eletrônico

valor = int(input("Quanto deseja sacar? R$"))
notas = [50, 20, 10, 1]
for nota in notas:
    qtd = valor // nota
    if qtd > 0:
        print(f"{qtd} cédula(s) de R${nota}")
    valor %= nota
