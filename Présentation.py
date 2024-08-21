import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.sidebar.success("Veuillez sélectionner une page")

st.markdown("<h1 style='text-align: center; font-size: 3em;'>🎯 Bienvenue dans BetControl!</h1>", unsafe_allow_html=True)

# Lien URL de la présentation Canva

canva_url = "https://www.canva.com/design/DAGOajikWjw/4bkqaYYBcp5jyhTExYuGpg/view?utm_content=DAGOajikWjw&utm_campaign=designshare&utm_medium=embeds&utm_source=link"


# Ajouter l'iframe dans Streamlit
st.components.v1.iframe(canva_url, width=800, height=600, scrolling=False)
