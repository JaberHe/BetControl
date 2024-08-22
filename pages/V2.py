import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

import streamlit as st

import streamlit as st

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
.cote-button {
    font-size: 1.2em;
    text-align: center;
    color: #f4d03f;
    margin-top: 10px;
    width: 100%; /* S'assurer que le bouton prend toute la largeur */
    background-color: #333333;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
    display: block;
}

/* Alignement des boutons pour les cotes */
.cotes-container {
    display: flex;
    justify-content: space-between;
}

/* Alignement centré pour les noms des joueurs */
.player-name {
    font-size: 1.2em;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Exemple de contenu pour les 3 matchs
matches = [
    {"player1": "Novak Djokovic", "player2": "Carlos Alcaraz", "odds": [1.43, 2.85]},
    {"player1": "Rafael Nadal", "player2": "Roger Federer", "odds": [1.50, 2.75]},
    {"player1": "Paris Saint-Germain", "player2": "Real Madrid", "odds": [1.70, 3.50, 4.00]}  # Exemple avec 3 cotes pour un match de foot
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
            <div class="cotes-container">
        """, unsafe_allow_html=True)
        
        # Affichage des cotes sous forme de boutons alignés en ligne
        for odd in match['odds']:
            st.markdown(f"""
            <button class="cote-button" onclick="alert('Vous avez choisi une cote de {odd} pour {match['player1']} vs {match['player2']}')">
                {odd}
            </button>
            """, unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

# Ligne de séparation
st.markdown("---")
