# SheetBot

Automatizador inteligente de arquivos CSV para Google Sheets.  
Projetado para validar, corrigir e sincronizar dados de produção em saúde pública de forma eficiente e segura.

---

## O que o SheetBot faz?

1. **Lê arquivos `.csv`** organizados por município
2. **Filtra dados e remove** registros irrelevantes
3. Gera **mensagens automáticas** de **correção com base em regras de regex**
4. **Envia os dados para a aba correta de uma planilha** Google Sheets via API
5. **Remove os arquivos** após o envio com sucesso

Desenvolvido inicialmente como ferramenta interna para agilizar demandas manuais do dia a dia.

---

## Requisitos

- Python 3.10 ou superior  
- Conta Google com permissão de edição na planilha  
- Credenciais da API do Google (conta de serviço)

---

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/sheetbot.git
cd sheetbot
````

### 2. Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração das Credenciais Google

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto e ative:

   * **Google Sheets API**
   * **Google Drive API**
3. Crie uma conta de serviço (`IAM & Admin > Service Accounts`)
4. Gere uma chave JSON da conta de serviço
5. Compartilhe a planilha do Google Sheets com o e-mail da conta de serviço com permissão de edição

---

## Arquivo `.env`

Crie um arquivo `.env` com as variáveis de ambiente:

```env
CAMINHO_CREDENCIAL=autenticacao/credentials.json
NOME_PLANILHA=Nome exato da sua planilha Google Sheets
```

---

## Como rodar

```bash
python main.py
```

O script irá:

* Criar as pastas necessárias
* Ler os CSVs em `relatorios-csv/{municipio}/`
* Tratar os dados e gerar mensagens de correção automáticas
* Enviar os dados para a aba correta da planilha
* Excluir os arquivos processados

---

## Estrutura de Diretórios

```
sheetbot/
├── main.py
├── .env
├── requirements.txt
├── autenticacao/
│   └── autenticar_google_sheets.py
├── modulos/
│   ├── deletar_csv.py
│   ├── enviar_para_planilha.py
│   ├── estrutura.py
│   ├── listar_csvs.py
│   ├── processar_municipio.py
│   ├── regras_correcao_regex.py
│   └── tratamento.py
└── relatorios-csv/
    ├── areia/
    ├── escada/
    ├── cabo/
    └── itacuruba/
```
---

## Possíveis Erros

* **403 PERMISSION\_DENIED**: verifique se a planilha foi compartilhada com o e-mail da conta de serviço
* **Erro de encoding**: certifique-se de que o CSV está em UTF-8
* **Dados não enviados**: confirme o nome do município e a existência da aba correspondente na planilha

---

## Autor

**Thiago Campello**
Desenvolvedor Python focado em automações e dados.

🔗 [Thiago Campello](https://www.linkedin.com/in/thiago-campello/)

📂 [github.com/Thiago-Campello/sheetbot](https://github.com/Thiago-Campello/sheetbot)

---


