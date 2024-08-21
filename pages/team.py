import pandas as pd
import streamlit as st

# Chargement des données
df_club = pd.read_csv("bet_equipe.csv")

# Fonction pour calculer les gains ou pertes
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
    return round(result, 2)

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Coup de coeur !</h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Choisissez votre équipe, votre mise et découvrez combien vous auriez gagné en pariant uniquement sur votre équipe </h3>", unsafe_allow_html=True)

st.markdown("---")  # Ligne de séparation pour plus de clarté

# Entrée pour la mise moyenne
mise = st.number_input('💰 Entrez votre mise moyenne (€):', min_value=0, step=1, format="%d")

# Créer une liste des équipes uniques
equipes = sorted(pd.concat([df_club['HomeTeam'], df_club['AwayTeam']]).unique())

# Liste déroulante des équipes
equipe = st.selectbox('Choisissez votre équipe', equipes)

st.markdown("---")  # Ligne de séparation

# Bouton pour soumettre le formulaire
if st.button('Calculer'):
    result = gain_équipe(equipe, mise)
    
    # Affichage du résultat
    st.write(f"💸 Pour une mise moyenne de **{mise}€**, vous auriez {'gagné' if result >= 0 else 'perdu'} **{abs(result)}€** en pariant sur **{equipe}**.")
