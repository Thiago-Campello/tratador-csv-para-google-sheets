import gspread
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

# Carrega a credencial da variável de ambiente
credencial_json = os.getenv("CAMINHO_CREDENCIAL")

# Define o escopo de permissões necessárias para acessar Google Sheets e Google Drive
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Cria credenciais com base no arquivo JSON e escopo definido
creds = ServiceAccountCredentials.from_json_keyfile_name(credencial_json, scope)

# Cria cliente autenticado para interagir com o Google Sheets
client = gspread.authorize(creds)
