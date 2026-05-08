import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Carrefour Smart Dashboard", layout="wide")

st.title("🛒 Carrefour Maroc : Dashboard Performance")
st.markdown("Analyse automatisée des **Offres Digitales & Trade Marketing**")

def load_data(file):
    # Lecture en sautant les lignes vides au début (skiprows)
    df = pd.read_csv(file, skiprows=1)
    # Nettoyage des lignes vides
    df = df.dropna(subset=[df.columns[2]])
    return df

# Menu de sélection sur le côté
st.sidebar.header("Configuration")
format_choisi = st.sidebar.radio("Choisir le format :", ["Hyper", "Market"])

# On définit le nom du fichier à lire
nom_fichier = "hyper.csv" if format_choisi == "Hyper" else "market.csv"

try:
    df = load_data(nom_fichier)
    
    # Statistiques rapides
    c1, c2 = st.columns(2)
    c1.metric("Nombre d'offres", len(df))
    c2.metric("Format sélectionné", format_choisi)

    # Graphique
    st.subheader("Répartition des offres")
    fig = px.bar(df, x=df.columns[2], title=f"Produits en promotion ({format_choisi})")
    st.plotly_chart(fig, use_container_width=True)

    # Affichage du tableau
    st.write("Détails des données :")
    st.dataframe(df)

except Exception as e:
    st.error(f"Erreur : Vérifie que le fichier {nom_fichier} est bien sur ton GitHub.")
