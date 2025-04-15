# Desafio 79 - Lista sem repetições

numeros = []
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Número adicionado!")
    else:
        print("Número duplicado! Não adicionado.")
    if input("Quer continuar? [S/N]").strip().upper() == 'N':
        break
print("Números digitados:", sorted(numeros))
