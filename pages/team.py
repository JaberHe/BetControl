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

st.markdown("---")  # Ligne de séparation

# Filtrer les équipes par sport
equipes_football = sorted(pd.concat([df_club[df_club['sport'] == 'Football']['HomeTeam'], df_club[df_club['sport'] == 'Football']['AwayTeam']]).unique())
equipes_basket = sorted(pd.concat([df_club[df_club['sport'] == 'Basket']['HomeTeam'], df_club[df_club['sport'] == 'Basket']['AwayTeam']]).unique())
equipes_tennis = sorted(pd.concat([df_club[df_club['sport'] == 'Tennis']['HomeTeam'], df_club[df_club['sport'] == 'Tennis']['AwayTeam']]).unique())

# Création de trois colonnes pour les différents sports
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚽ Football")
    equipe_football = st.selectbox('Choisissez votre équipe de football', [""] + equipes_football)

with col2:
    st.markdown("### 🏀 Basket")
    equipe_basket = st.selectbox('Choisissez votre équipe de basket', [""] + equipes_basket)

with col3:
    st.markdown("### 🎾 Tennis")
    equipe_tennis = st.selectbox('Choisissez votre équipe de tennis', [""] + equipes_tennis)

st.markdown("---")  # Ligne de séparation

# Bouton pour soumettre le formulaire
if st.button('Calculer'):
    # Prioriser la sélection de l'équipe dans l'ordre des sports
    if equipe_football:
        equipe_selectionnee = equipe_football
    elif equipe_basket:
        equipe_selectionnee = equipe_basket
    else:
        equipe_selectionnee = equipe_tennis
    
    # Calculer le résultat
    result = gain_équipe(equipe_selectionnee, mise)
    
    # Affichage du résultat
    st.write(f"💸 Pour une mise moyenne de **{mise}€**, vous auriez {'gagné' if result >= 0 else 'perdu'} **{abs(result)}€** en pariant sur **{equipe_selectionnee}**.")
