sexo=str(input('Sexo[M/F]:').upper().strip()[0])
while sexo not in 'MF':
     sexo=input('Dados invalidos!Por favor digite um sexo valido:').strip().upper()[0]
print('Sexo {} resgistrado com sucesso!'.format(sexo))