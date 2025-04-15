ex=str(input("Digite a expressão:"))
cont1=ex.count("(")
cont2=ex.count(")")
if cont1 == cont2:
    print('Sua expressão esta valida')
else:
    print('Expressão invalida')