import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.sidebar.success("Veuillez sélectionner une page")

st.markdown("<h1 style='text-align: center; font-size: 3em;'>🎯 Bienvenue dans BetControl!</h1>", unsafe_allow_html=True)


# Lien de partage ou iframe de Canva
canva_presentation_url = "https://www.canva.com/design/DAGOajikWjw/4bkqaYYBcp5jyhTExYuGpg/view"  # Remplace par le lien de partage Canva

# Si tu as un lien de partage, tu peux créer l'iframe comme ceci :
iframe_code = f"""
<iframe src="{canva_presentation_url}" width="800" height="600" frameborder="0" allowfullscreen></iframe>
"""

# Utilisation de la fonction `components.html` pour intégrer l'iframe
st.components.v1.html(iframe_code, height=600)

# Lien URL de la présentation Canva

#canva_url = "https://www.canva.com/design/DAGOajikWjw/4bkqaYYBcp5jyhTExYuGpg/view"

# Ajouter l'iframe dans Streamlit
#st.components.v1.iframe(canva_url, width=800, height=600, scrolling=False)
