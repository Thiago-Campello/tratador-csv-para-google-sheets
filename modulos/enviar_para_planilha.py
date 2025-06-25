import os
from dotenv import load_dotenv
from autenticacao.autenticar_google_sheets import client
from gspread_dataframe import set_with_dataframe

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define o nome da planilha a partir da variável de ambiente
planilha = os.getenv("NOME_PLANILHA")
spreadsheet = client.open(planilha)

# Função responsável por enviar um DataFrame para a aba correspondente do município
def enviar_para_planilha(municipio, df):

    # Seleciona a aba correspondente ao município
    abas = {
        'escada': 0,
        'cabo': 1,
        'itacuruba': 2,
        'areia': 3,
        'teste': 4
    }
    try:
        sheet = spreadsheet.get_worksheet(abas.get(municipio))
        print(f'Aba selecionada: {municipio}')

    except Exception:
        print(f'Município {municipio} não reconhecido!')
    

    # Tenta enviar os dados para a aba correspondente
    try:
        last_line = len(sheet.get_all_values()) + 1  # Descobre a próxima linha disponível
        set_with_dataframe(sheet, df, row=last_line, include_column_header=False)  # Envia os dados
        print(f"Dados enviados para a aba de {municipio}")
    except Exception as e:
        print(f"Erro ao enviar dados para {municipio}: {e}")
