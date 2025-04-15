# Desafio 76 - Lista de preços

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)
print("-"*40)
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<30} R${produtos[i+1]:>7.2f}")
print("-"*40)
