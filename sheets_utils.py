import gspread
import streamlit as st
from google.oauth2.service_account import Credentials
import json

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


@st.cache_resource
def connect_to_gsheet():
    # Tenta usar as credenciais do Streamlit Secrets (modo deploy)
    if st.secrets.get("gcp_service_account"):
        service_account_info = st.secrets["gcp_service_account"]
    else:
        # Modo local: carrega o JSON salvo no projeto
        with open("gymme-gains-c8a467f8722b.json") as source:
            service_account_info = json.load(source)

    credentials = Credentials.from_service_account_info(
        service_account_info,
        scopes=SCOPES
    )
    client = gspread.authorize(credentials)
    sheet = client.open("GymPlannerData").sheet1
    return sheet


def adicionar_treino(nome_usuario, exercicios):
    sheet = connect_to_gsheet()
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
