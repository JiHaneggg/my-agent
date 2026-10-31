
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 1. .env 파일 불러오기
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# 2. OpenAI API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# 3. API 키 존재 여부 확인
if not api_key:
    st.error("OPENAI_API_KEY를 찾을 수 없습니다.")
    st.stop()

# 4. LangChain 모델 객체 생성
model = init_chat_model(
    "gpt-5.4-mini",
    model_provider="openai",
    api_key=api_key
)

st.title("AI 챗봇")

prompt = st.chat_input("질문을 입력하세요.")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = model.invoke(prompt)
        st.write(response.content)
