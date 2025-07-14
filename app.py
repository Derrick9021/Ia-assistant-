import streamlit as st
import pyttsx3
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

# Configuration voix
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

# Chargement du contenu
@st.cache_resource
def load_index():
    documents = SimpleDirectoryReader('docs').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

# Interface
st.set_page_config(page_title="Assistant PV", layout="centered")
st.title("🔆 Assistant Vocal des Modules PV")
st.markdown("Pose-moi une question sur les panneaux solaires.")

index = load_index()
query_engine = index.as_query_engine()

question = st.text_input("💬 Pose ta question ici")

if question:
    response = query_engine.query(question)
    st.write("🧠 **Réponse :**", response.response)

    if st.button("🔊 Écouter la réponse"):
        engine.say(response.response)
        engine.runAndWait()
