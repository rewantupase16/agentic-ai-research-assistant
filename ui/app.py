import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import run_agent

st.set_page_config(page_title="Rewant", layout="centered")
st.title("Rewant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Render existing messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message immediately
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        response = run_agent(prompt)
        st.write(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})

    st.rerun()
