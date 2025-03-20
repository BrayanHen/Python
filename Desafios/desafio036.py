vc=float(input('Qual o valor da casa?:'))
sal=float(input('Qual o salario do comprador?:'))
anos=int(input('Em quantos anos a casa vai ser paga?:'))

prestaçao= vc/(anos*12)

#valor da casa dividido pelos meses que a casa sera paga = prestaçao por mes da casa

print('Para financiar a casa em {} anos a prestação sera de R${:.2f}'.format(anos,prestaçao))

if prestaçao > sal*30/100:
    print('Seu emprestimo foi NEGADO.')
else:
    print('Seu emprestimo foi APROVADO!')

print('Tenha um bom dia!')