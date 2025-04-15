# Desafio 82 - Dividindo valores em listas diferentes

numeros = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if input("Quer continuar? [S/N]").strip().upper() == 'N':
        break
print(f"Lista completa: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")
