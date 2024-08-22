import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

# Exemple de contenu pour les 3 matchs
matches = [
    {"player1": "Novak Djokovic", "player2": "Carlos Alcaraz", "odds": [1.43, 2.85]},
    {"player1": "Rafael Nadal", "player2": "Roger Federer", "odds": [1.50, 2.75]},
    {"player1": "Paris Saint-Germain", "player2": "Real Madrid", "odds": [1.70, 3.50, 4.00]}  # Exemple avec 3 cotes pour un match de foot
]

# Affichage des 3 matchs en colonnes
col1, col2, col3 = st.columns(3)

selected_odds = []  # Liste pour enregistrer les cotes sélectionnées

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
                # Créer un bouton pour chaque cote
                if st.button(str(odd), key=f"{match['player1']}_{match['player2']}_{odd}"):
                    selected_odds.append((match['player1'], match['player2'], odd))

# Afficher les cotes sélectionnées
if selected_odds:
    st.markdown("### Cotes sélectionnées")
    for selection in selected_odds:
        st.write(f"Match: {selection[0]} vs {selection[1]} - Cote sélectionnée: {selection[2]}")
