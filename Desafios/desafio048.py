total = 0
cont = 0
for c in range(1,501):
    if c % 3 == 0 and c % 2==1:
      cont +=  1
      total += c
print('A soma de todos os {} valores solicitados é {}'.format(cont,total))


# c % 3 == 0 == multiplo de 3 , c % 2 == 1 == par
# += somar e atribuir