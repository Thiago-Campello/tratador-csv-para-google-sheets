import pandas as pd
import chardet
import re
from modulos.regras_correcao_regex import regras_de_correcao_regex

# Detecta o encoding do arquivo para garantir leitura correta
def detectar_encoding(caminho):
    with open(caminho, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def gerar_correcao(row):
    tipo = row['Tipo da Ficha']
    erros = f"{row['Validações de Regras Negócio']} {row['Validações de Campos Obrigatórios']}".lower()
    
    regras = regras_de_correcao_regex.get(tipo, [])

    for regex, mensagem in regras:
        if re.search(regex, erros):
            #print(f'Mensagem introduzida com sucesso! {mensagem}')
            return mensagem

    #print('Sem mensagem para o erro!')
    return ''

# Lê, trata e retorna um DataFrame com colunas filtradas
def tratar_csv(caminho):
    try:
        encoding = detectar_encoding(caminho)
        df = pd.read_csv(caminho, encoding=encoding, sep=';')

        # Remove registros com erros estruturais duplicados
        df = df[~df['Erros Estruturais'].str.lower().str.contains('duplicadas', na=False)]


        # Define a estrutura completa de colunas, de A até K
        colunas_em_ordem = [
            'Data de Recebimento',       # A
            'Tipo da Ficha',             # B
            'UUID',                      # C
            'Validações de Regras Negócio',  # D
            'Validações de Campos Obrigatórios', # E
            'Situação da Análise',       # F
            'Nome Profissional',         # G
            'Unidade',                   # H
            'Analista',                  # I
            'Data Contato',              # J
            'Correção'                   # K
        ]

        # Cria um DataFrame com as colunas até a K
        df_final = pd.DataFrame(columns=colunas_em_ordem)


        # Copia os valores para as colunas A-E
        df_final[['Data de Recebimento', 'Tipo da Ficha', 'UUID',
                  'Validações de Regras Negócio', 'Validações de Campos Obrigatórios']] = df[
            ['Data de Recebimento', 'Tipo da Ficha', 'UUID',
             'Validações de Regras Negócio', 'Validações de Campos Obrigatórios']
        ].copy()


        # Aplicando o tratamento de inconsistências na coluna K
        df_final['Correção'] = df_final.apply(gerar_correcao, axis=1)

        return df_final
    except Exception as e:
        print(f"Erro ao tratar CSV: {e}")
        return None