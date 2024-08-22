import streamlit as st

# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'> Quel parieur es-tu ? </h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Nous allons te proposer plusieurs paris par question, clique sur la cote qui t'intéresse le plus !  </h3>", unsafe_allow_html=True)

# Exemple avec deux box côte à côte
col1, col2, col3 = st.columns(3)  # Trois colonnes côte à côte

# Première boxe
with col1:
    match_info = {
        'date': "Aujourd'hui à 18:15",
        'event': 'US Open',
        'player1': 'Novak Djokovic',
        'player2': 'Carlos Alcaraz',
        'odds_player1': 1.70,
        'odds_player2': 2.10
    }

    st.markdown(f" {match_info['player1']} vs {match_info['player2']}")
    st.markdown(f" {match_info['event']}")
    
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
        'event': 'NBA',
        'player1': 'Serena Williams',
        'player2': 'Naomi Osaka',
        'odds_player1': 1.75,
        'odds_player2': 2.10
    }

    st.markdown(f" {match_info2['player1']} vs {match_info2['player2']}")
    st.markdown(f" {match_info['event']}")
    
    # Colonnes pour les cotes
    col2_1, col2_2 = st.columns(2)
    
    with col2_1:
        if st.button(f"{match_info2['odds_player1']} (Serena)"):
            st.success(f"Vous avez choisi {match_info2['player1']} avec une cote de {match_info2['odds_player1']}.")
    
    with col2_2:
        if st.button(f"{match_info2['odds_player2']} (Osaka)"):
            st.success(f"Vous avez choisi {match_info2['player2']} avec une cote de {match_info2['odds_player2']}.")

with col3:
    match_info3 = {
        'date': "Aujourd'hui à 20:00",
        'event': 'Ligue 1',
        'player1': 'Paris SG',
        'player2': 'Montpellier',
        'odds_player1': 1.29,
        'odds_player2': 8.50,
        'odds_draw' : 6 
    }

    st.markdown(f" {match_info2['player1']} vs {match_info2['player2']}")
    st.markdown(f" {match_info['event']}")
    
    # Colonnes pour les cotes
    col2_1, col2_2, col2_3 = st.columns(3)
    
    with col2_1:
        if st.button(f"{match_info2['odds_player1']} "):
            st.success(f"Vous avez choisi {match_info3['player1']} avec une cote de {match_info2['odds_player1']}.")
    
    with col2_2:
        if st.button(f"{match_info2['odds_player2']}"):
            st.success(f"Vous avez choisi {match_info3['player2']} avec une cote de {match_info2['odds_player2']}.")

    with col2_3:
        if st.button(f"{match_info2['odds_draw']}"):
            st.success(f"Vous avez choisi le match nul avec une cote de {match_info3['odds_player2']}.")

# Ligne de séparation et espace pour la mise en page
st.markdown("---")

# CSS personnalisé pour le design
st.markdown("""
<style>
/* Style de la box principale */
.box {
    background-color: #1e1e1e;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 20px;
}

/* Style pour la ligne "Pari combiné" */
.header {
    font-size: 1.5em;
    text-align: center;
    margin-bottom: 10px;
    background-color: #333333;
    padding: 10px;
    border-radius: 10px;
    color: white;
}

/* Style pour les box imbriquées */
.sub-box {
    background-color: #2e2e2e;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: white;
}

/* Style pour les cotes */
.cote {
    font-size: 1.2em;
    text-align: right;
    color: #f4d03f;
}
</style>
""", unsafe_allow_html=True)

# Affichage du titre principal de la box "Pari combiné"
st.markdown("<div class='header'>Pari combiné</div>", unsafe_allow_html=True)

# Conteneur pour la première box imbriquée
with st.container():
    st.markdown("<div class='sub-box'><b>Pavel Kotov - Lorenzo Sonego</b><br>Vainqueur: <b>P. Kotov</b><span class='cote'>2,20</span></div>", unsafe_allow_html=True)

# Conteneur pour la deuxième box imbriquée
with st.container():
    st.markdown("<div class='sub-box'><b>Rinky Hijikata - David Goffin</b><br>Vainqueur: <b>D. Goffin</b><span class='cote'>1,60</span></div>", unsafe_allow_html=True)

# Ajout d'un bouton de soumission
if st.button('Valider ce combiné'):
    st.success("Vous avez validé votre pari combiné.")
