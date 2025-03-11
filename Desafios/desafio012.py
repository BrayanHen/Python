s=float(input('Qual é o salario do funcionario?:R$'))
ns=s + (s*15/100)

input("Um funcionario q recebia R${},com 15% de aumento,passara a receber R${:.2f}".format(s, ns))