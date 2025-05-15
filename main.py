import streamlit as st

st.title("🧠 나와 닮은 수학자는 누구일까?")
st.markdown("MBTI를 입력하면 당신과 닮은 수학자를 알려드릴게요!")

mbti = st.selectbox("MBTI를 선택하세요", [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

if st.button("결과 보기"):
    st.success(f"당신은 {mbti} 유형입니다!")
