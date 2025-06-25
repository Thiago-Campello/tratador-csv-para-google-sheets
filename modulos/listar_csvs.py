import os

# Lista os caminhos dos arquivos CSV dentro da pasta do município informado
def listar_csvs(municipio):
    arquivos = []
    diretorio = os.path.join("relatorios-csv", municipio)

    # Percorre os arquivos da pasta e adiciona os caminhos à lista
    for arquivo in os.listdir(diretorio):
        dir_path = os.path.join(diretorio, arquivo)

        if not os.path.exists(dir_path):
            print(f"Arquivo não encontrado: {dir_path}")
            continue

        arquivos.append(dir_path)
        print(f'Lendo arquivo: {dir_path}')
    
    return arquivos