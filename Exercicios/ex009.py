for c in range(1,4):
    print('=========={}° Aluno==========='.format(c))
    nome=input('Nome:')

    nota=int(input('Nota do aluno em portugues:'))
    med+=nota

    nota1=int(input('Nota do aluno em matematica:'))
    med+=nota1

    nota2=int(input('Nota do aluno em ciencias:'))
    med += nota2

    med = 0
    media = med / 3
    print('A media do aluno é:{:1.2f}'.format(media))


