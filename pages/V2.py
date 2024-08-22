import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

# Exemple avec deux box côte à côte
col1, col2 = st.columns(2)  # Deux colonnes côte à côte

# Première boxe
with col1:
    match_info = {
        'date': "Aujourd'hui à 18:15",
        'event': 'ATP - US Open, Qualifications',
        'player1': 'Novak Djokovic',
        'player2': 'Carlos Alcaraz',
        'odds_player1': 1.43,
        'odds_player2': 2.85
    }

    st.markdown(f"#### {match_info['player1']} vs {match_info['player2']}")
    
    # Colonnes pour les cotes
    col1_1, col1_2 = st.columns(2)
    
    with col1_1:
        if st.button(f"{match_info['odds_player1']} (Djokovic)"):
            st.success(f"Vous avez choisi {match_info['player1']} avec une cote de {match_info['odds_player1']}.")
    
    with col1_2:
        if st.button(f"{match_info['odds_player2']} (Alcaraz)"):
            st.success(f"Vous avez choisi {match_info['player2']} avec une cote de {match_info['odds_player2']}.")

# Deuxième boxe
with col2:
    match_info2 = {
        'date': "Aujourd'hui à 20:00",
        'event': 'WTA - US Open, Qualifications',
        'player1': 'Serena Williams',
        'player2': 'Naomi Osaka',
        'odds_player1': 1.75,
        'odds_player2': 2.10
    }

    st.markdown(f"#### {match_info2['player1']} vs {match_info2['player2']}")
    
    # Colonnes pour les cotes
    col2_1, col2_2 = st.columns(2)
    
    with col2_1:
        if st.button(f"{match_info2['odds_player1']} (Serena)"):
            st.success(f"Vous avez choisi {match_info2['player1']} avec une cote de {match_info2['odds_player1']}.")
    
    with col2_2:
        if st.button(f"{match_info2['odds_player2']} (Osaka)"):
            st.success(f"Vous avez choisi {match_info2['player2']} avec une cote de {match_info2['odds_player2']}.")

# Ligne de séparation et espace pour la mise en page
st.markdown("---")
