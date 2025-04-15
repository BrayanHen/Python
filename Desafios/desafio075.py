# Desafio 75 - Análise de números em tupla

num = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))
print(f"O número 9 apareceu {num.count(9)} vezes")
print(f"O número 3 apareceu na posição {num.index(3)+1 if 3 in num else 'nenhuma'}")
print("Números pares digitados:", [n for n in num if n % 2 == 0])
