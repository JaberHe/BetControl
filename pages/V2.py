import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

import streamlit as st

# Utiliser st.session_state pour stocker les sélections de cotes
if 'selected_odds' not in st.session_state:
    st.session_state.selected_odds = {}

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
    align-items: center;
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
    width: 90%; /* Ajuste la largeur pour un bon alignement */
    margin: 5px; /* Espacement autour */
}

</style>
""", unsafe_allow_html=True)

# Exemple de contenu pour les 6 matchs
matches = [
    {"player1": "Novak Djokovic", "player2": "Carlos Alcaraz", "odds": [1.43, 2.85]},
    {"player1": "Rafael Nadal", "player2": "Roger Federer", "odds": [1.50, 2.75]},
    {"player1": "Paris Saint-Germain", "player2": "Real Madrid", "odds": [1.70, 3.50, 4.00]},
    {"player1": "Serena Williams", "player2": "Naomi Osaka", "odds": [1.60, 2.20]},
    {"player1": "Andy Murray", "player2": "Stefanos Tsitsipas", "odds": [1.80, 2.10]},
    {"player1": "Iga Swiatek", "player2": "Aryna Sabalenka", "odds": [1.55, 2.40]}
]

# Affichage des 6 matchs en 2 rangées de 3 colonnes
for i in range(0, len(matches), 3):
    col1, col2, col3 = st.columns(3)

    for col, match in zip([col1, col2, col3], matches[i:i+3]):
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
            for j, odd in enumerate(match['odds']):
                with cols[j]:
                    if st.button(f"{odd}", key=f"{match['player1']}_{match['player2']}_{odd}"):
                        # Stocker la cote sélectionnée pour ce match
                        st.session_state.selected_odds[f"{match['player1']}_{match['player2']}"] = {"odd": odd, "player1": match['player1'], "player2": match['player2']}

# Affichage de la dernière sélection
st.markdown("### Sélection actuelle")
if st.session_state.selected_odds:
    last_selected_match = list(st.session_state.selected_odds.keys())[-1]
    last_selected_info = st.session_state.selected_odds[last_selected_match]
    st.write(f"Match: {last_selected_info['player1']} vs {last_selected_info['player2']} - Cote sélectionnée: {last_selected_info['odd']}")

# Ligne de séparation
st.markdown("---")
