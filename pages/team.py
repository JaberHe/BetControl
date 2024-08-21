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
st.markdown("""
<style>
/* Boutons non sélectionnés */
div.stRadio > div > label > div {
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

/* Boutons sélectionnés */
div.stRadio > div > label > div[data-selected="true"] {
    background-color: #f4d03f;
    color: black;
}

/* Supprimer le point radio natif */
div.stRadio > div > label > input {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# Liste des équipes (exemple)
equipes = ['Lyon', 'Real Madrid', 'Villarreal', 'Celta Vigo']

# Entrée pour la mise moyenne
mise = st.number_input('💰 Entrez votre mise moyenne (€):', min_value=0, step=1, format="%d")

# Afficher les boutons des équipes avec st.radio
equipe_selected = st.radio("Sélectionnez votre équipe:", equipes)

# Vérification de l'équipe sélectionnée et affichage du résultat
if equipe_selected is not None:
    st.success(f"Équipe sélectionnée: {equipe_selected}")
    result = gain_équipe(equipe_selected, mise)
    st.write(f"🎯 Pour une mise moyenne de {mise}€, vous auriez {'gagné' if result >= 0 else 'perdu'} {abs(result)}€ avec {equipe_selected}.")
