import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

import streamlit as st

# Simuler des données pour plusieurs matchs
matches = [
    {"player1": "Novak Djokovic", "player2": "Carlos Alcaraz", "odds": [1.43, 2.85], "sport": "Tennis"},
    {"player1": "Rafael Nadal", "player2": "Roger Federer", "odds": [1.50, 2.75], "sport": "Tennis"},
    {"player1": "Paris Saint-Germain", "player2": "Real Madrid", "odds": [1.70, 3.50, 4.00], "sport": "Football"},
    {"player1": "Serena Williams", "player2": "Naomi Osaka", "odds": [1.60, 2.20], "sport": "Tennis"},
    {"player1": "Andy Murray", "player2": "Stefanos Tsitsipas", "odds": [1.80, 2.10], "sport": "Tennis"},
    {"player1": "Iga Swiatek", "player2": "Aryna Sabalenka", "odds": [1.55, 2.40], "sport": "Tennis"}
]

# Initialiser les variables dans st.session_state
if 'current_block' not in st.session_state:
    st.session_state.current_block = 0  # Index du bloc actuel
if 'selections' not in st.session_state:
    st.session_state.selections = {}  # Stocker les sélections par match

# Afficher le bloc actuel de 3 matchs
block_size = 3
start_index = st.session_state.current_block * block_size
end_index = start_index + block_size

# Afficher les matchs actuels
for match in matches[start_index:end_index]:
    match_key = f"{match['player1']} vs {match['player2']}"
    st.markdown(f"### {match['player1']} vs {match['player2']}")
    st.markdown(f"**Sport:** {match['sport']}")
    cols = st.columns(len(match['odds']))
    for i, odd in enumerate(match['odds']):
        if cols[i].button(f"{odd}"):
            # Stocker ou mettre à jour la sélection pour ce match
            st.session_state.selections[match_key] = {
                "player1": match['player1'],
                "player2": match['player2'],
                "selected_odd": odd,
                "sport": match['sport']
            }

# Affichage du bouton "Suivant" si toutes les cotes du bloc sont sélectionnées
if len(st.session_state.selections) >= (st.session_state.current_block + 1) * block_size:
    if st.button("Voir les 3 matchs suivants"):
        st.session_state.current_block += 1
        st.experimental_rerun()  # Redémarrer l'application avec le bloc suivant

# Affichage des sélections (dernière sélection par match)
st.markdown("### Vos sélections actuelles")
for match_key, selection in st.session_state.selections.items():
    st.write(f"Match: {selection['player1']} vs {selection['player2']}, Cote: {selection['selected_odd']}, Sport: {selection['sport']}")

# Fin de l'affichage des blocs
if st.session_state.current_block >= len(matches) // block_size:
    st.markdown("### Vous avez terminé de sélectionner les cotes pour tous les matchs.")
