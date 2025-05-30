import google.generativeai as genai
import streamlit as st

def get_gemini_response(prompt):
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
        if not api_key:
            return "❌ API key not found. Please set GOOGLE_API_KEY in .streamlit/secrets.toml."

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}" 