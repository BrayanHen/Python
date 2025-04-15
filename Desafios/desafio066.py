cont=0
c=0
while True:
    num=int(input('Digite um valor (999 para parar):'))
    c+=1
    cont+=num
    if num == 999:
        break
print(f'A soma dos {c-1} valores foi {cont-999}')