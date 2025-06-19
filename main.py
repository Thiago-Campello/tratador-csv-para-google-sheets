from modulos.processar_municipio import processar_municipio
from modulos.estrutura import criar_pastas

def main():
    criar_pastas()

    municipios = ['escada', 'cabo', 'itacuruba', 'areia', 'teste']

    for municipio in municipios:
        print(f"🚀 Iniciando processamento de {municipio}...")

        processar_municipio(municipio)

        print(f"✅ Processamento de {municipio} finalizado.\n")

if __name__=='__main__':
    main()