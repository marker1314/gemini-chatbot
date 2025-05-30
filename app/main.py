import streamlit as st
from app.ui import render_ui
from app.gemini_api import get_gemini_response
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Gemini Chatbot")

user_input = render_ui()

if user_input:
    response = get_gemini_response(user_input)
    st.markdown("### 🤖 Gemini says:")
    st.write(response) 