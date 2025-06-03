# 🧹 Tratador de CSV para Google Sheets

Este projeto automatiza o processo de:
1. **Leitura de arquivos CSV** organizados por município.
2. **Tratamento e filtragem** de dados relevantes.
3. **Envio automático para abas específicas** de uma planilha no Google Sheets.

Foi desenvolvido como ferramenta pessoal para agilizar demandas internas, e está disponível no GitHub para que colegas da empresa também possam utilizá-lo facilmente.

---

## 🚀 Requisitos

- Python 3.10 ou superior  
- Conta Google com permissão de edição na planilha destino  
- Cada usuário deve possuir **suas próprias credenciais** da API do Google

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Thiago-Campello/tratador-csv-para-google-sheets.git
cd tratador-csv-para-google-sheets
````

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração das Credenciais Google

Cada usuário deve:

1. Acessar [Google Cloud Console](https://console.cloud.google.com/).
2. Criar um projeto e ativar as seguintes APIs:

   * Google Sheets API
   * Google Drive API
3. Ir em **IAM & Admin > Service Accounts**, criar uma nova conta de serviço.
4. Gerar e baixar a chave JSON da conta de serviço.
5. **Compartilhar a planilha do Google Sheets com o e-mail da conta de serviço** (ex: `xxxx@xxxx.iam.gserviceaccount.com`) com permissão de edição.

> ⚠️ Por questões de segurança, **não compartilhe sua credencial com outras pessoas.**

---

## 📁 Estrutura de Diretórios

```
tratador-csv-para-google-sheets/
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
│   └── tratamento.py
├── relatorios-csv/
│   ├── escada/
│   ├── cabo/
│   └── itacuruba/
```

---

## ⚙️ Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
CAMINHO_CREDENCIAL=autenticacao/credentials.json
NOME_PLANILHA=Nome exato da sua planilha no Google Sheets
```

---

## ▶️ Como Rodar

Execute o script principal:

```bash
python main.py
```

O script irá:

* Criar as pastas necessárias (caso não existam).
* Ler os CSVs dentro de `relatorios-csv/{municipio}/`.
* Tratar os dados, removendo entradas desnecessárias.
* Enviar os dados para a aba correta da planilha.
* Excluir os arquivos após o envio.

---

## 🛟 Possíveis Problemas

* **403 PERMISSION\_DENIED**: verifique se a planilha foi compartilhada com a conta de serviço correta.
* **Erro de encoding**: os arquivos CSV devem estar em UTF-8 ou similar.
* **Dados não enviados**: verifique se o nome do município está correto e se a aba correspondente existe na planilha.

---

## 👥 Autor

* [Thiago Campello](https://github.com/Thiago-Campello)

---


