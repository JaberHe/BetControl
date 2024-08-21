import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.sidebar.success("Veuillez sélectionner une page")

st.markdown("<h1 style='text-align: center; font-size: 3em;'>🎯 Bienvenue dans BetControl!</h1>", unsafe_allow_html=True)

st.html(""" 
        
        <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGOajikWjw&#x2F;4bkqaYYBcp5jyhTExYuGpg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGOajikWjw&#x2F;4bkqaYYBcp5jyhTExYuGpg&#x2F;view?utm_content=DAGOajikWjw&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">currency</a> par JABER
       
        
         """)
# Lien URL de la présentation Canva

canva_url = "https://www.canva.com/design/DAGOajikWjw/4bkqaYYBcp5jyhTExYuGpg/view?utm_content=DAGOajikWjw&utm_campaign=designshare&utm_medium=embeds&utm_source=link"


# Ajouter l'iframe dans Streamlit
st.components.v1.iframe(canva_url, width=800, height=600, scrolling=False)
