import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)


# CSS personnalisé pour améliorer le design
st.markdown("""
<style>
/* Style pour les box avec bordure rouge */
.match-box {
    background-color: #1e1e1e; /* Couleur de fond */
    padding: 20px;
    border-radius: 10px;
    border: 2px solid red; /* Bordure rouge fine */
    margin-bottom: 20px;
}

/* Centrage du texte */
.centered-text {
    text-align: center;
    font-size: 1.2em;
    color: white;
}

/* Alignement centré pour les cotes */
.cote {
    font-size: 1.5em;
    text-align: center;
    color: #f4d03f;
    margin-top: 10px;
}

/* Alignement centré pour les noms des joueurs */
.player-name {
    font-size: 1.5em;
    text-align: center;
    color: white;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# Exemple de contenu pour les 3 matchs
matches = [
    {"player1": "Novak Djokovic", "player2": "Carlos Alcaraz", "odds_player1": 1.43, "odds_player2": 2.85},
    {"player1": "Rafael Nadal", "player2": "Roger Federer", "odds_player1": 1.50, "odds_player2": 2.75},
    {"player1": "Serena Williams", "player2": "Naomi Osaka", "odds_player1": 1.60, "odds_player2": 2.20}
]

# Affichage des 3 matchs en colonnes
col1, col2, col3 = st.columns(3)

for col, match in zip([col1, col2, col3], matches):
    with col:
        st.markdown(f"""
        <div class="match-box">
            <div class="player-name">{match['player1']}</div>
            <div class="player-name">vs</div>
            <div class="player-name">{match['player2']}</div>
            <div class="cote">{match['odds_player1']} | {match['odds_player2']}</div>
        </div>
        """, unsafe_allow_html=True)

# Bouton pour chaque match, avec alignement centré
with col1:
    if st.button(f"Cote {matches[0]['odds_player1']}"):
        st.success(f"Vous avez choisi {matches[0]['player1']} avec une cote de {matches[0]['odds_player1']}.")

with col2:
    if st.button(f"Cote {matches[1]['odds_player1']}"):
        st.success(f"Vous avez choisi {matches[1]['player1']} avec une cote de {matches[1]['odds_player1']}.")

with col3:
    if st.button(f"Cote {matches[2]['odds_player1']}"):
        st.success(f"Vous avez choisi {matches[2]['player1']} avec une cote de {matches[2]['odds_player1']}.")

# Ligne de séparation
st.markdown("---")
