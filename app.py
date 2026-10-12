import streamlit as st
from dotenv import load_dotenv

from config.settings import PAGE_TITLE
from ui.styles import load_css
from ui.sidebar import render_sidebar
from prompts.system_prompt import SYSTEM_PROMPT
from services.groq_service import ask_groq

load_dotenv()

st.set_page_config(
    page_title=PAGE_TITLE,
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

render_sidebar()

st.title("DevOps Knowledge Assistant")

st.write(
    "Guidance, troubleshooting support, and learning assistance across the DevOps lifecycle."
)

prompt = st.chat_input(
    "Ask a DevOps question..."
)

if prompt:

    with st.spinner("Generating response..."):

        answer = ask_groq(
            prompt,
            SYSTEM_PROMPT
        )

        st.write(answer)