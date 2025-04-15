# Desafio 70 - Cadastro de produtos

total = caro = barato = 0
barato_nome = ''
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$"))
    total += preco
    if preco > 1000:
        caro += 1
    if barato == 0 or preco < barato:
        barato = preco
        barato_nome = nome
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
print(f"Total gasto: R${total:.2f}")
print(f"{caro} produtos custam mais de R$1000")
print(f"Produto mais barato: {barato_nome} (R${barato:.2f})")
