import streamlit as st

def render_ui():
    st.title("💬 Gemini Chatbot")
    st.write("Ask me anything!")

    user_input = st.text_area("Your message:", height=150)
    if st.button("Send"):
        return user_input
    return None 