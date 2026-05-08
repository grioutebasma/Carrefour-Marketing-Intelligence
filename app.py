import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Carrefour Dashboard", layout="wide")
st.title("🛒 Carrefour Maroc : Dashboard Performance")

# Cette fonction liste les fichiers pour être sûr de ce qu'on lit
files_in_repo = os.listdir('.')
st.sidebar.write("Fichiers détectés :", files_in_repo)

def load_data(file_name):
    # On force la lecture du fichier présent
    df = pd.read_csv(file_name, skiprows=1)
    df = df.dropna(subset=[df.columns[1]])
    return df

format_choisi = st.sidebar.radio("Choisir le format :", ["Hyper", "Market"])

# On s'adapte aux noms exacts sur ton GitHub
if format_choisi == "Hyper":
    target = "hyper.csv"
else:
    target = "market.csv"

if target in files_in_repo:
    try:
        df = load_data(target)
        st.success(f"Données {format_choisi} chargées !")
        st.plotly_chart(px.bar(df, x=df.columns[1], title="Analyse des promotions"))
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur de lecture : {e}")
else:
    st.error(f"Le fichier {target} est introuvable. Vérifie bien le nom sur GitHub.")
