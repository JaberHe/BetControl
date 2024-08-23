import pandas as pd
import streamlit as st

# Chargement des données
df_club = pd.read_csv("bet_equipe.csv")

# Dictionnaire de correspondance des abréviations d'équipes NBA avec leurs noms complets
nba_teams = {
    "hou": "Houston Rockets",
    "lal": "Los Angeles Lakers",
    "bos": "Boston Celtics",
    "mia": "Miami Heat",
    "gs": "Golden State Warriors",
    "den" : "Denver Nuggets",
    "min" : "Minnessota Timberwolwes",
    "mem" : "Memphis Grizzlies",
    "lac" : "Los Angeles Clippers",
    "sa" : "San Antonio Spurs",
    "utah" : "Utah Jazz",
    "orl" : "Orlando Magic",
    "sac" : "Sacramento Kings",
    "no" : "New Orleans Pelicans",
    "ny" : "New York Knicks",
    "bkn" : "Brooklyn Nets",
    "ind" : "Indiana Pacers",
    "okc" : "Oklahoma City Thunder",
    "phx" : "Phoenix Suns",
    "chi" : "Chicago Bulls",
    "cha" : "Charlotte Hornets",
    "phi" : "Philadelpie Sixers",
    "por" : "Portland Trailblazzers",
    "cle" : "Cleveland Cavaliers",
    "wsh" : "Washington Wizzards",
    "dal" : "Dallas Mavericks",
    "det" : "Detroit Pistons",
    "tor" : "Toronto Raptors",
    "mil" : "Milwaukee Bucks",
    "atl" : "Atlanta Hawks"
    # Ajoute ici toutes les autres correspondances
}

# Remplacer les abréviations par les noms complets dans les colonnes HomeTeam, AwayTeam et vainqueur pour les équipes de basket
df_club.loc[df_club['sport'] == 'basket', 'HomeTeam'] = df_club.loc[df_club['sport'] == 'basket', 'HomeTeam'].replace(nba_teams)
df_club.loc[df_club['sport'] == 'basket', 'AwayTeam'] = df_club.loc[df_club['sport'] == 'basket', 'AwayTeam'].replace(nba_teams)
df_club.loc[df_club['sport'] == 'basket', 'vainqueur'] = df_club.loc[df_club['sport'] == 'basket', 'vainqueur'].replace(nba_teams)

# Fonction pour calculer les gains ou pertes, le nombre de matchs, et les dates des premiers et derniers matchs
def gain_équipe(equipe, mise):
    win = 0
    loss = 0
    dates = []
    
    for index, row in df_club.iterrows():
        if row["vainqueur"] == equipe:
            win = win + row["odd_W"]
        if equipe in row["HomeTeam"] or equipe in row["AwayTeam"]:
            loss = loss + 1
            dates.append(row["Date"])  # Utilisation du nom correct de la colonne
    
    balance = win - loss
    result = balance * mise
    
    if dates:  # Si la liste des dates n'est pas vide
        first_match_date = min(dates)  # Date du premier match
        last_match_date = max(dates)   # Date du dernier match
    else:
        first_match_date = last_match_date = None
    
    return round(result, 2), loss, first_match_date, last_match_date

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Coup de coeur ❤️</h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Choisissez votre équipe ou votre joueur de tennis préféré, renseignez votre mise et découvrez combien vous auriez gagné ou perdu en pariant uniquement sur votre équipe ou joueur de coeur </h3>", unsafe_allow_html=True)

st.markdown("---")  # Ligne de séparation pour plus de clarté

# Entrée pour la mise moyenne
mise = st.number_input('💰 Entrez votre mise moyenne (€):', min_value=0, step=1, format="%d")

st.markdown("---")  # Ligne de séparation

# Nettoyer et filtrer les équipes par sport, en supprimant les doublons
equipes_football = sorted(pd.concat([df_club[df_club['sport'] == 'football']['HomeTeam'], 
                                     df_club[df_club['sport'] == 'football']['AwayTeam']]).map(str.strip).unique())
equipes_basket = sorted(pd.concat([df_club[df_club['sport'] == 'basket']['HomeTeam'], 
                                   df_club[df_club['sport'] == 'basket']['AwayTeam']]).map(str.strip).unique())
equipes_tennis = sorted(pd.concat([df_club[df_club['sport'] == 'tennis']['HomeTeam'], 
                                   df_club[df_club['sport'] == 'tennis']['AwayTeam']]).map(str.strip).unique())

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
    equipe_tennis = st.selectbox('Choisissez votre joueur de tennis', [""] + equipes_tennis)

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
    result, num_matches, first_match_date, last_match_date = gain_équipe(equipe_selectionnee, mise)
    
    # Affichage du résultat
    st.write(f"💸 Pour une mise de **{mise}€**, vous auriez {'gagné' if result >= 0 else 'perdu'} **{abs(result)}€** en pariant sur **{equipe_selectionnee}**.")
    st.write(f"Vous auriez misé sur **{num_matches}** matchs.")
    if first_match_date and last_match_date:
        st.write(f"Le premier match a eu lieu le **{first_match_date}** et le dernier match le **{last_match_date}**.")
