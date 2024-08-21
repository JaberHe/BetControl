import pandas as pd
import numpy as np
import streamlit as st
from itertools import product

# Chargement des données
df = pd.read_csv("df_final.csv")

#region Fonctions

def calculate_losses_for_single_bet(sport, odds):
    """
    Calcul des pertes pour un pari simple
    """
    win = 0
    loss = 0
    nb_match = 0

    # Parcourir les lignes du DataFrame
    for index, row in df.iterrows():
        if row["odd_W"] in odds and row["sport"] in sport:
            win += (row["odd_W"] - 1)
            nb_match += 1

        if row["odd_L_1"] in odds and row["sport"] in sport:
            loss -= 1
            nb_match += 1

        if row["odd_L_2"] in odds and row["sport"] in sport:
            loss -= 1
            nb_match += 1

    coef = (win + loss) / nb_match
    perte = -(mise_moy * freq_sem * 52 * coef)
    return round(perte, 2)

def calculate_losses_for_multiple_bets(df, sport, odds_interval, mise_moy, freq_sem, nb_selec):
    """
    Calcul des pertes pour des paris multiples
    """
    iterations = 1000
    total_result = 0
    total_nb_paris = 0

    # Filtrer le DataFrame
    df_filtered = df[
        (df['odd_W'].between(odds_interval.left, odds_interval.right)) |
        (df['odd_L_1'].between(odds_interval.left, odds_interval.right)) |
        (df['odd_L_2'].between(odds_interval.left, odds_interval.right)) &
        (df['sport'].isin(sport))
    ]

    if len(df_filtered) < nb_selec:
        return 0

    # Boucle d'itération pour simuler les paris
    for _ in range(iterations):
        sampled_df = df_filtered.sample(n=nb_selec, replace=True)

        win = np.prod(sampled_df['odd_W'].values) if all(sampled_df['odd_W'].between(odds_interval.left, odds_interval.right)) else 0

        all_combinations = [
            [odds for odds in row[['odd_W', 'odd_L_1', 'odd_L_2']] if odds_interval.left <= odds <= odds_interval.right]
            for _, row in sampled_df.iterrows()
        ]

        all_paths = list(product(*all_combinations))
        nb_paris = len(all_paths)

        if nb_paris > 0:
            result_df = win - nb_paris
            total_result += result_df
            total_nb_paris += nb_paris

    average_weighted_coefficient = total_result / total_nb_paris if total_nb_paris > 0 else 0

    perte = -(mise_moy * freq_sem * 52 * average_weighted_coefficient)
    return round(perte, 2)

#endregion

#----------------------------------------------------------------------------

#Début de streamlit

#----------------------------------------------------------------------------


#st.markdown(
    """
    <style>
    .st-cq {
        border: 1px solid green;  
        background-color : green;
    }

    .st-emotion-cache-1vzeuhh {
    background-color: green;
    
    }
    .st-e7 {
        background: linear-gradient(to right, green 0%, green 20%, rgba(172, 177, 195, 0.25) 20%, rgba(172, 177, 195, 0.25) 100%);
    color : green;
    }
    .st-e8 {
        background: linear-gradient(to right, green 0%, green 40%, rgba(172, 177, 195, 0.25) 40%, rgba(172, 177, 195, 0.25) 100%);
    color : green;
    }
    .st-e9 {
        background: linear-gradient(to right, green 0%, green 60%, rgba(172, 177, 195, 0.25) 60%, rgba(172, 177, 195, 0.25) 100%);
    color : green;
    }
    .st-ea {
    background: linear-gradient(to right, green 0%, green 80%, rgba(172, 177, 195, 0.25) 80%, rgba(172, 177, 195, 0.25) 100%);
    color : green;
    }
    .st-eb {
    background: linear-gradient(to right, green 0%, green 100%, rgba(172, 177, 195, 0.25) 100%, rgba(172, 177, 195, 0.25) 100%);
    color : green;
    }
    .st-emotion-cache-10y5sf6 {
    
    color: green;
    }
    .st-emotion-cache-15hul6a:hover {
        border: 1px solid green;
        color : green;
    }

    .focused.st-emotion-cache-19cfm8f.e116k4er3 {
     border: 1px solid green;
    }

    </style>
    """,
    unsafe_allow_html=True
#)

# Injecter du JavaScript pour forcer la couleur verte après le chargement


# Titre principal de l'application avec un style plus grand
st.markdown("<h1 style='text-align: center; font-size: 3em;'>🎯 Bienvenue dans BetControl!</h1>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h3 style='text-align: center;'>Répondez à ce formulaire pour savoir combien vous avez économisé.</h3>", unsafe_allow_html=True)

st.markdown("---")  # Ligne de séparation pour plus de clarté

# Sélection des sports préférés
st.write('### Sélection des Sports')
football = st.checkbox("⚽ Football", key='football')
basket = st.checkbox("🏀 Basket", key='basket')
tennis = st.checkbox("🎾 Tennis", key='tennis')

sports = []
if football:
    sports.append("football")
if basket:
    sports.append("basket")
if tennis:
    sports.append("tennis")

# Affichage des sports sélectionnés avec un style en gras
if sports:
    st.markdown(f'📅 **Sports sélectionnés:** {", ".join(sports)}')
else:
    st.markdown('🚫 **Aucun sport sélectionné.**')

st.markdown("---")  # Ligne de séparation

# Slider pour le nombre de sélections
nb_selec = st.slider(
    'Combien de sélections mettez-vous en moyenne sur vos paris (ex: 1 (simple) 1+ (multiple))',
    min_value=1,
    max_value=6,
    value=1,
    help="Choisissez le nombre moyen de sélections par pari"
)

st.markdown("---")  # Ligne de séparation

# Sélection des cotes
st.write('### Sélection des cotes')
categorie_cotes = st.radio(
    'Choisissez une catégorie de cotes :',
    (
        'Grands favoris [inf 1.4]',
        'Légers favoris [1.4 - 1.8]',
        'Côtes moyennes [1.8 - 2.5]',
        'Légers outsiders [2.5 - 4]',
        'Grands outsiders [sup 4]'
    )
)

# Définir odds_lower et odds_upper en fonction de la catégorie sélectionnée
if categorie_cotes == 'Grands favoris [inf 1.4]':
    odds_lower, odds_upper = 1, 1.4
elif categorie_cotes == 'Légers favoris [1.4 - 1.8]':
    odds_lower, odds_upper = 1.4, 1.8
elif categorie_cotes == 'Côtes moyennes [1.8 - 2.5]':
    odds_lower, odds_upper = 1.8, 2.5
elif categorie_cotes == 'Légers outsiders [2.5 - 4]':
    odds_lower, odds_upper = 2.5, 4
elif categorie_cotes == 'Grands outsiders [sup 4]':
    odds_lower, odds_upper = 4, 120

st.write(f'📊 Vous avez sélectionné la catégorie: **{categorie_cotes}**')

st.markdown("---")  # Ligne de séparation

# Entrée pour la mise moyenne
mise_moy = st.number_input('💰 Entrez votre mise moyenne (€):', min_value=0, step=1, format="%d")

# Entrée pour la fréquence des paris
freq_sem = st.number_input('📅 Entrez votre fréquence de paris (par semaine):', min_value=0)

# Détermination de l'intervalle de cotes
odds = pd.Interval(left=odds_lower, right=odds_upper, closed='both')

st.markdown("---")  # Ligne de séparation


# Bouton pour soumettre le formulaire
if st.button('Soumettre le formulaire'):

    # Détermination du nombre d'itérations basé sur les cotes
    iterations = 10000 if odds_lower >= 4 else 1000

    # Calcul des pertes potentielles
    if nb_selec == 1:
        result = calculate_losses_for_single_bet(sports, odds)
    else:
        result = calculate_losses_for_multiple_bets(df, sports, odds, mise_moy, freq_sem, nb_selec)

    # Affichage du résultat
    st.write(f"💸 Pour une mise moyenne de **{mise_moy}€** et **{freq_sem}** paris par semaine, vous allez perdre en moyenne **{result}€** par an !")