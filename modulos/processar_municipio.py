from modulos.deletar_csv import deletar_csv
from modulos.listar_csvs import listar_csvs
from modulos.tratamento import tratar_csv
from modulos.enviar_para_planilha import enviar_para_planilha


def processar_municipio(municipio):
    # Lista os arquivos CSV do município e processa cada um
    try:
        arquivos = listar_csvs(municipio)
        for arquivo in arquivos:
            df = tratar_csv(arquivo)
            if df is None or df.empty:
                print(f'DataFrame de {municipio} vazio.')
                continue
            enviar_para_planilha(municipio, df)
            deletar_csv(arquivo)
            
    except Exception as e:
        print(f'Falha ao processar {municipio}.', e)