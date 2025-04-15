# Desafio 80 - Lista ordenada sem sort()

lista = []
for _ in range(5):
    num = int(input("Digite um número: "))
    if not lista or num > lista[-1]:
        lista.append(num)
    else:
        for i, v in enumerate(lista):
            if num <= v:
                lista.insert(i, num)
                break
print("Lista ordenada:", lista)
