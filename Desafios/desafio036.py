vc=float(input('Qual o valor da casa?:'))
sal=float(input('Qual o salario do comprador?:'))
anos=float(input('Em quantos anos a casa vai ser paga?:'))

prestacao= vc /12
valor=prestacao*30/100

if prestacao > valor:
    print('Seu emprestimo foi negado.')
else:
    print('Seu emprestimo foi aprovado!')
print('Tenha um bom dia!')