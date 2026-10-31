
import streamlit as st

st.set_page_config(
    page_title="My Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My Agent")
st.write("나만의 AI Agent 프로젝트")

st.divider()

user_input = st.text_input("질문을 입력하세요")

if st.button("실행"):
    if user_input.strip():
        st.success("입력 완료!")
        st.write(f"입력한 질문: {user_input}")
    else:
        st.warning("질문을 먼저 입력해주세요.")
