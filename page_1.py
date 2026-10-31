
import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv

from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# .env 파일 불러오기 (추가)
load_dotenv(Path(__file__).resolve().parent / ".env")

# API 키 확인 (추가)
if not os.getenv("OPENAI_API_KEY"):
    st.error("OpenAI API 키가 없습니다.")
    st.stop()

if not os.getenv("TAVILY_API_KEY"):
    st.error("Tavily API 키가 없습니다.")
    st.stop()

# 모델 객체
model = init_chat_model("gpt-5.4-mini")

# Tavily 검색 도구
tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
)

# Agent 생성
agent = create_agent(model, tools=[tavily_tool])

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("우리 회사 챗봇")

prompt = st.chat_input("여기에 입력하시오.")

if prompt:
    response = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["messages"][-1].content
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
