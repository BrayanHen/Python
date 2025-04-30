from ex115.lib.arquivo import *

arq='cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('\033[35mNovo Cadastro\033[m')
        nome=str(input('Nome:'))
        idade=leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[35m Saindo do sistema...\033[m')
        break
    else:
        print('\033[31mErro! digite uma opção valida!\033[m')

