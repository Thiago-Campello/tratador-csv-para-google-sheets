import os

def criar_pastas():
    base_path = os.path.join(os.getcwd(), "relatorios-csv")

    # Cria a pasta principal 'relatorios-csv', se não existir
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"📁 Pasta principal criada: {base_path}")
    else:
        print(f"📁 Pasta principal já existe: {base_path}")

    # Subpastas que serão criadas dentro da pasta principal
    subpastas = ['escada', 'cabo', 'itacuruba']

    for pasta in subpastas:
        caminho_completo = os.path.join(base_path, pasta)
        if not os.path.exists(caminho_completo):
            os.makedirs(caminho_completo)
            print(f"📁 Subpasta criada: {caminho_completo}")
        else:
            print(f"📁 Subpasta já existe: {caminho_completo}")