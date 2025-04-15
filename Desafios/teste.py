import os

desafios = {
    'desafio101.py','desafio102.py','desafio103.py','desafio104.py','desafio105.py','desafio106.py','desafio107.py','desafio108.py','desafio109.py','desafio110.py','desafio111.py','desafio111.py''desafio112.py','desafio113.py','desafio114.py'
}

for arquivo in desafios:
    with open(arquivo, "w", encoding="utf-8") as f:
        print(f"Arquivo {arquivo} criado com sucesso!")


