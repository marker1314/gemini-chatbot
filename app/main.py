import streamlit as st
from dotenv import load_dotenv
import os
from gemini_api import get_gemini_response

load_dotenv()
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")

# 세션 히스토리 초기화
if "history" not in st.session_state:
    st.session_state.history = []

st.title("💬 Gemini Chatbot")

# 기존 대화 표시
for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)

# 사용자 입력
user_input = st.chat_input("Ask something...")

if user_input:
    # 사용자 메시지 출력
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Gemini 응답 생성
    with st.chat_message("assistant"):
        response = get_gemini_response(user_input)
        st.markdown(response)
        st.session_state.history.append(("assistant", response))  