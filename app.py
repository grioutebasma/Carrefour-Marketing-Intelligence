import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuration de la page
st.set_page_config(page_title="Carrefour Dashboard BI", layout="wide")

st.title("🛒 Carrefour Maroc : Dashboard Performance")
st.markdown("Analyse automatisée des **Offres Digitales & Trade Marketing**")

# Fonction pour charger les données avec le bon encodage
def load_data(file_name):
    # 'latin-1' permet de lire les accents et symboles sans erreur
    df = pd.read_csv(file_name, skiprows=1, encoding='latin-1')
    # On supprime les lignes totalement vides
    df = df.dropna(how='all')
    return df

# Barre latérale pour la navigation
st.sidebar.header("Menu de Configuration")

# Détection des fichiers présents sur GitHub
files_present = os.listdir('.')
format_choisi = st.sidebar.radio("Choisir le format de magasin :", ["Hyper", "Market"])

# Sélection du fichier correspondant
target_file = "hyper.csv" if format_choisi == "Hyper" else "market.csv"

# Vérification et affichage
if target_file in files_present:
    try:
        data = load_data(target_file)
        
        # 1. Indicateurs clés (KPIs)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Nombre d'articles en promotion", len(data))
        with col2:
            st.metric("Format analysé", format_choisi)

        # 2. Graphique interactif
        st.subheader(f"Analyse visuelle des offres - {format_choisi}")
        # On utilise la deuxième colonne pour le graphique (souvent la catégorie ou le produit)
        fig = px.histogram(data, x=data.columns[1], 
                           title=f"Répartition des offres par catégorie ({format_choisi})",
                           color_discrete_sequence=['#003399']) # Bleu Carrefour
        st.plotly_chart(fig, use_container_width=True)

        # 3. Tableau de données complet
        with st.expander("Voir le détail des données brutes"):
            st.dataframe(data)

    except Exception as e:
        st.error(f"Erreur lors de l'analyse du fichier : {e}")
else:
    st.error(f"Le fichier {target_file} est introuvable sur GitHub. Vérifie bien le nom.")

# Signature pour ton SFE
st.sidebar.markdown("---")
st.sidebar.info("Développé pour le projet SFE - Digital Marketing & BI")
