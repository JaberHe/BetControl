import pandas as pd
import numpy as np
import streamlit as st
from itertools import product

# Chargement des données
df_club = pd.read_csv("bet_equipe.csv")

# Fonction 

def gain_équipe(equipe, mise):
  win = 0
  loss = 0
  for index, row in df_club.iterrows():
    if row["vainqueur"] == equipe:
      win = win + row["odd_W"] 
    if equipe in row["HomeTeam"] or equipe in row["AwayTeam"]:
      loss = loss + 1 
  balance = win - loss
  result = balance * mise
  return round(result,2)

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Coup de coeur !</h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Choisissez votre équipe, votre mise et découvrez combien vous auriez gagner en pariant uniquement sur votre équipe </h3>", unsafe_allow_html=True)

st.markdown("---")  # Ligne de séparation pour plus de clarté

# CSS pour personnaliser les boutons
import streamlit as st

# CSS pour personnaliser les options radio comme des boutons
import streamlit as st

# CSS pour personnaliser les options radio comme des boutons
import streamlit as st

# CSS pour personnaliser les options radio comme des boutons
import streamlit as st

# CSS pour masquer complètement les indicateurs radio natifs et personnaliser les options
import streamlit as st

# CSS pour personnaliser les boutons comme des cases
st.markdown("""
<style>
/* Boutons non sélectionnés */
div[data-testid="stVerticalBlock"] > div {
    background-color: #2f7738;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    margin: 5px;
    font-size: 18px;
    text-align: center;
    transition: background-color 0.3s ease;
    cursor: pointer;
}

/* Bouton sélectionné */
div[data-testid="stVerticalBlock"] > div[selected=true] {
    background-color: #f4d03f;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Liste des équipes (exemple)
equipes = ['Lyon', 'Real Madrid', 'Villarreal', 'Celta Vigo']

# Gérer la sélection via l'état de session
if 'selected_team' not in st.session_state:
    st.session_state.selected_team = None

# Entrée pour la mise moyenne
mise = st.number_input('💰 Entrez votre mise moyenne (€):', min_value=0, step=1, format="%d")

# Créer une grille de boutons
cols = st.columns(2)  # 2 colonnes
for i, equipe in enumerate(equipes):
    col = cols[i % 2]  # Alterner entre les colonnes
    if col.button(equipe, key=equipe):
        st.session_state.selected_team = equipe

# Afficher le résultat du calcul si une équipe est sélectionnée
if st.session_state.selected_team:
    st.success(f"Équipe sélectionnée: {st.session_state.selected_team}")
    result = gain_équipe(st.session_state.selected_team, mise)
    st.write(f"🎯 Pour une mise moyenne de {mise}€, vous auriez {'gagné' if result >= 0 else 'perdu'} {abs(result)}€ avec {st.session_state.selected_team}.")
