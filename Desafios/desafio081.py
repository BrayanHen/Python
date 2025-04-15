# Desafio 81 - Extraindo dados de uma lista

numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))
    if input("Quer continuar? [S/N]").strip().upper() == 'N':
        break
print(f"Quantidade de elementos digitados: {len(numeros)}")
print(f"Lista ordenada de forma decrescente: {sorted(numeros, reverse=True)}")
print(f"O valor 5 {'' if 5 in numeros else 'não '}está na lista")
