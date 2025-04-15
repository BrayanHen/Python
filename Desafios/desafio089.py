# Desafio 89 - Boletim escolar

alunos = []
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    if input("Quer continuar? [S/N] ").strip().upper() == 'N':
        break
print(f"{'Nº':<4}{'Nome':<10}{'Média':>8}")
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
