from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except :
        print('Erro ao criar arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())

def cadastrar(arq,nome, idade):
    try:
        a=open(arq,'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
      try:
        a.write(f'{nome:<30}{idade:>3} anos\n')
      except:
         print('Erro ao escrever os dados!')
      else:
          print(f'Novo registro de {nome} adicionado com sucesso!')
          a.close()