import gspread
import json
from google.oauth2.service_account import Credentials
import streamlit as st

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

@st.cache_resource
def connect_to_gsheet():
    try:
        service_account_info = st.secrets["gcp_service_account"]
        credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPE)
    except:
        with open("credentials.json") as source:
            service_account_info = json.load(source)
        credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPE)
    client = gspread.authorize(credentials)
    sheet = client.open("GymPlannerData").sheet1
    return sheet

def adicionar_treino(nome_usuario, exercicios):
    sheet = connect_to_gsheet()  # ou crie a conexão aqui diretamente, se preferir
    print(exercicios)
    for ex in exercicios:
        linha = [
            nome_usuario,
            ex["Exercise"],
            ex["Sets"],
            ex["Reps"],
            ex["Rest"],
            ex["Weight"]
        ]
        sheet.append_row(linha, value_input_option="USER_ENTERED")