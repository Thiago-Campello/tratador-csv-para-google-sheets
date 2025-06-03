import pandas as pd
import chardet

# Detecta o encoding do arquivo para garantir leitura correta
def detectar_encoding(caminho):
    with open(caminho, 'rb') as f:
        return chardet.detect(f.read())['encoding']
    
# Lê, trata e retorna um DataFrame com colunas filtradas
def tratar_csv(caminho):
    try:
        encoding = detectar_encoding(caminho)
        df = pd.read_csv(caminho, encoding=encoding, sep=';')

        # Remove registros com erros estruturais duplicados
        df = df[~df['Erros Estruturais'].str.lower().str.contains('duplicadas', na=False)]

        # Seleciona apenas as colunas relevantes
        df = df[['Data de Recebimento', 'Tipo da Ficha', 'UUID', 'Validações de Regras Negócio', 'Validações de Campos Obrigatórios']]

        return df
    except Exception as e:
        print(f"⚠️ Erro ao tratar CSV: {e}")
        return None