import os


def deletar_csv(caminho_dir):
    try:
        # Deleta o arquivo CSV passado como parâmetro
        os.remove(caminho_dir)
        
        print(f'🗑️ Arquivo removido com sucesso!')
    except Exception as e:
        print(f'🚨 Erro ao deletar arquivo {caminho_dir}: {e}')