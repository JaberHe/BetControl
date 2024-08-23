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


st.markdown(
    """
    <style>
    p, ol, ul, dl {
    margin: 0px 10px 1rem;
    padding: 0px;
    font-size: large;
    font-weight: 600;
}
    
.st-emotion-cache-qrm19w p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: large;
}

.st-bj {
    margin-top: -0.7rem;
}

.st-bl {
    margin-right: -135px;
}

.st-cq {
    /* background-color: rgb(41, 105, 31); */
}

.st-e9 {
     background-image: none
}

.st-an {
    height: 3rem;
    width: 10rem;
}

.st-emotion-cache-4l3iyp{
    margin-left: 250px

}
    </style>
    """,
    unsafe_allow_html=True
)

# Injecter du JavaScript pour forcer la couleur verte après le chargement


# Titre principal de l'application avec un style plus grand
st.markdown("<h2 style='text-align: center; font-size: 3em;'>Bienvenue dans BetControl !</h2>", unsafe_allow_html=True)

# Sous-titre avec une police plus petite et espacée
st.markdown("<h4 style='text-align: center;'>Définissez votre profil parieur en répondant aux questions suivantes. L'algorithme BetControl appliquera alors vos habitudes de jeu sur plus de 75 000 matchs et calculera vos espérances de gains en fonction de votre profil. </h4>", unsafe_allow_html=True)

st.markdown("---")  # Ligne de séparation pour plus de clarté

# Sélection des sports préférés
# Sélection des sports préférés
st.write('#### Sur quels sports aimez-vous pariez ?')
st.write('Vous pouvez choisir plusieurs sports')

# Créer trois colonnes
col1, col2, col3 = st.columns(3)

# Placer un bouton dans chaque colonne


col1, col2, col3 = st.columns(3)

# Align checkboxes in columns
football = col1.checkbox("⚽ Football", key='football')
basket = col2.checkbox("🏀 Basket", key='basket')
tennis = col3.checkbox("🎾 Tennis", key="tennis")

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

st.write('#### Pari simple ou pari combiné ?')
# Slider pour le nombre de sélections
nb_selec = st.slider(
    'Combien de sélection mettez-vous en moyenne dans vos paris ? ',
    min_value=1,
    max_value=6,
    value=1,
    help="Choisissez le nombre moyen de sélections par pari"
)

st.markdown("---")  # Ligne de séparation



# Sélection des cotes
st.write('#### Favo ou surprise ?')
categorie_cotes = st.radio(
    'Quand vous pariez, sur quel type de cote préférez-vous cliquer ?',
    (
        'Gros favoris - cotes inférieures à 1,4',
        'Légers favoris - cotes comprises entre 1,4 et 1,8',
        'Cotes moyennes - cotes comprises entre 1,8 et 2,5',
        'Légers outsiders - cotes comprises entre 2,5 et 4',
        'Grosse surprise - cotes supérieures à 4'
    )
)

# Définir odds_lower et odds_upper en fonction de la catégorie sélectionnée
if categorie_cotes == 'Gros favoris - cotes inférieures à 1,4':
    odds_lower, odds_upper = 1, 1.4
elif categorie_cotes == 'Légers favoris - cotes comprises entre 1,4 et 1,8':
    odds_lower, odds_upper = 1.4, 1.8
elif categorie_cotes == 'Cotes moyennes - cotes comprises entre 1,8 et 2,5':
    odds_lower, odds_upper = 1.8, 2.5
elif categorie_cotes ==  'Légers outsiders - cotes comprises entre 2,5 et 4':
    odds_lower, odds_upper = 2.5, 4
elif categorie_cotes == 'Grosse surprise - cotes supérieures à 4':
    odds_lower, odds_upper = 4, 120

st.write(f'📊 Vous avez sélectionné la catégorie : **{categorie_cotes}**')

st.markdown("---")  # Ligne de séparation

# Entrée pour la mise moyenne
mise_moy = st.number_input('💰 Combien misez-vous en moyenne par pari ?', min_value=0, step=1, format="%d")

# Entrée pour la fréquence des paris
freq_sem = st.number_input('📅 Combien de paris faites-vous en moyenne par semaine ?', min_value=0)

# Détermination de l'intervalle de cotes
odds = pd.Interval(left=odds_lower, right=odds_upper, closed='both')

st.markdown("---")  # Ligne de séparation


# Bouton pour soumettre le formulaire
if st.button('Lancer le calcul'):

    # Détermination du nombre d'itérations basé sur les cotes
    iterations = 10000 if odds_lower >= 4 else 1000

    # Calcul des pertes potentielles
    if nb_selec == 1:
        result = calculate_losses_for_single_bet(sports, odds)
    else:
        result = calculate_losses_for_multiple_bets(df, sports, odds, mise_moy, freq_sem, nb_selec)

    # Affichage du résultat
    st.write(f"💸 Pour une mise moyenne de **{mise_moy}€** et **{freq_sem}** paris par semaine, vous allez perdre en moyenne **{result}€** par an !")
