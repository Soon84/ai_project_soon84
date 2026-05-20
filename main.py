import streamlit as st


st.title("AI 협업 개발 실습")
st.write("첫 번째 Streamlit 앱입니다.")

st.divider()

st.info("이름을 입력하고 실습 시작 버튼을 눌러보세요.")

name = st.text_input("이름을 입력하세요")

if st.button("실습 시작"):
    if name:
        st.success(f"{name}님, 환영합니다! AI 협업 개발 실습을 시작해볼까요?")
    else:
        st.warning("이름을 먼저 입력해주세요.")
