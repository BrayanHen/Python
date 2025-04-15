# Desafio 74 - Sorteio de números e análise

from random import randint
numeros = tuple(randint(1, 10) for _ in range(5))
print("Números sorteados:", numeros)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
