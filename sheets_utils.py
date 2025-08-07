import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

@st.cache_resource
def connect_to_gsheet():
    credentials = Credentials.from_service_account_file(
        'credentials.json',  # Ou use st.secrets se for deploy no Streamlit Cloud
        scopes=SCOPES
    )
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
