import ollama
import streamlit as st

st.title("MUSA")

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)


