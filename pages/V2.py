import pandas as pd
import streamlit as st


# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs pari par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

import streamlit as st

# Données d'exemple
match_info = {
    'date': "Aujourd'hui à 18:15",
    'event': 'ATP - US Open, Qualifications',
    'player1': 'Novak Djokovic',
    'player2': 'Carlos Alcaraz',
    'odds_player1': 1.43,
    'odds_player2': 2.85
}


# Structure de la boxe avec les deux joueurs et les cotes
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(f"#### {match_info['player1']}")

with col2:
    st.markdown(f"#### {match_info['player2']}")

# Colonnes pour les cotes
col1, col2 = st.columns(2)

# Affichage des cotes et boutons pour chaque joueur
with col1:
    if st.button(f"{match_info['odds_player1']}"):
        st.success(f"Vous avez choisi {match_info['player1']} avec une cote de {match_info['odds_player1']}.")

with col2:
    if st.button(f"{match_info['odds_player2']}"):
        st.success(f"Vous avez choisi {match_info['player2']} avec une cote de {match_info['odds_player2']}.")

# Ligne de séparation et espace pour la mise en page
st.markdown("---")
