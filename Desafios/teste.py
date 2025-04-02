import os
import shutil

# Define o intervalo de números para as pastas
inicio = 66
fim = 90

# Loop para excluir as pastas
target_directory = os.getcwd()  # Diretório atual, pode ser alterado
for i in range(inicio, fim + 1):
    pasta_nome = f"desafio{i:03d}"  # Formato desafio066, desafio067, ...
    caminho_completo = os.path.join(target_directory, pasta_nome)

    try:
        if os.path.exists(caminho_completo) and os.path.isdir(caminho_completo):
            shutil.rmtree(caminho_completo)
            print(f"Pasta removida: {caminho_completo}")
        else:
            print(f"Pasta não encontrada: {caminho_completo}")
    except Exception as e:
        print(f"Erro ao remover a pasta {pasta_nome}: {e}")
