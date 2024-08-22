import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

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

/* Alignement centré pour les noms des joueurs */
.player-name {
    font-size: 1.2em;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

/* Style pour centrer les cotes */
.cote-button-container {
    display: flex;
    justify-content: center;
}

.cote-button {
    font-size: 1.2em;
    text-align: center;
    color: #f4d03f;
    background-color: #333333;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
    width: 80%; /* Ajuste la largeur pour un bon alignement */
    margin-top: 5px; /* Espacement au-dessus */
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
        </div>
        """, unsafe_allow_html=True)
        
        # Utilisation de colonnes pour aligner les cotes sur une seule ligne
        cols = st.columns(len(match['odds']))
        for i, odd in enumerate(match['odds']):
            with cols[i]:
                st.markdown(f"""
                <div class="cote-button-container">
                    <button class="cote-button">{odd}</button>
                </div>
                """, unsafe_allow_html=True)

# Ligne de séparation
st.markdown("---")

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

/* Alignement centré pour les noms des joueurs */
.player-name {
    font-size: 1.2em;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

/* Style pour centrer les cotes */
.cote-button-container {
    display: flex;
    justify-content: center;
}

.cote-button {
    font-size: 1.2em;
    text-align: center;
    color: #f4d03f;
    background-color: #333333;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
    width: 80%; /* Ajuste la largeur pour un bon alignement */
    margin-top: 5px; /* Espacement au-dessus */
}

</style>
""", unsafe_allow_html=True)

# Exemple de contenu pour les 3 matchs
matches_1 = [
    {"player1": "Simona Halep", "player2": "Iga Swiatek", "odds": [1.75, 2.2]},
    {"player1": "Houston Rockets", "player2": "New_York Knicks", "odds": [1.80, 1.85]},
    {"player1": "Marseille", "player2": "Rennes", "odds": [1.85, 3.30, 3.75]}  # Exemple avec 3 cotes pour un match de foot
]

# Affichage des 3 matchs en colonnes
col11, col22, col33 = st.columns(3)

for col, match in zip([col11, col22, col33], matches_1):
    with col:
        st.markdown(f"""
        <div class="match-box">
            <div class="player-name">{match['player1']}</div>
            <div class="player-name">vs</div>
            <div class="player-name">{match['player2']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Utilisation de colonnes pour aligner les cotes sur une seule ligne
        cols = st.columns(len(match['odds']))
        for i, odd in enumerate(match['odds']):
            with cols[i]:
                st.markdown(f"""
                <div class="cote-button-container">
                    <button class="cote-button">{odd}</button>
                </div>
                """, unsafe_allow_html=True)

# Ligne de séparation
st.markdown("---")
