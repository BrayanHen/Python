# Desafio 78 - Maior e menor valor em lista

valores = [int(input(f"Digite um valor para a posição {i}: ")) for i in range(5)]
print(f"Maior valor {max(valores)} na posição {valores.index(max(valores))}")
print(f"Menor valor {min(valores)} na posição {valores.index(min(valores))}")
