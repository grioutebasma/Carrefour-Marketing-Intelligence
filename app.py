import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Carrefour Dashboard BI", layout="wide")

st.title("🛒 Carrefour Maroc : Dashboard Performance")
st.markdown("Analyse automatisée des **Offres Digitales & Trade Marketing**")

def load_data(file_name):
    # Correction : ajout de sep=';' pour les fichiers CSV Excel
    df = pd.read_csv(file_name, skiprows=1, encoding='latin-1', sep=';')
    df = df.dropna(how='all')
    return df

st.sidebar.header("Menu de Configuration")
files_present = os.listdir('.')
format_choisi = st.sidebar.radio("Choisir le format de magasin :", ["Hyper", "Market"])

target_file = "hyper.csv" if format_choisi == "Hyper" else "market.csv"

if target_file in files_present:
    try:
        data = load_data(target_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Nombre d'articles en promotion", len(data))
        with col2:
            st.metric("Format analysé", format_choisi)

        st.subheader(f"Analyse visuelle des offres - {format_choisi}")
        # On vérifie qu'il y a assez de colonnes pour le graphique
        if len(data.columns) > 1:
            fig = px.histogram(data, x=data.columns[1], 
                               title=f"Répartition des offres ({format_choisi})",
                               color_discrete_sequence=['#003399'])
            st.plotly_chart(fig, use_container_width=True)

        with st.expander("Voir le détail des données brutes"):
            st.dataframe(data)

    except Exception as e:
        st.error(f"Erreur lors de l'analyse du fichier : {e}")
else:
    st.error(f"Le fichier {target_file} est introuvable sur GitHub.")

st.sidebar.markdown("---")
st.sidebar.info("Développé pour le projet SFE - Digital Marketing & BI")
