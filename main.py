import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌈", layout="centered")

# 🎉 상단 메뉴 (외부 의존 없이)
menu_items = ["MBTI로 직업 찾기", "앱 소개", "문의하기"]
selected = st.sidebar.radio("✨ 탐색 메뉴", menu_items)

# 🧠 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🔬 과학자", "📊 전략 컨설턴트", "💻 데이터 과학자"],
    # ... (생략: 앞 예시와 동일)
    "ESFP": ["🎬 배우", "🕺 댄서", "🎤 가수"],
}

if selected == "MBTI로 직업 찾기":
    st.markdown(
        "<h1 style='text-align: center; color: #e67e22;'>🌈 MBTI로 알아보는 나의 진로 ✨</h1>",
        unsafe_allow_html=True
    )
    st.markdown("#### 당신의 MBTI는 무엇인가요? 😍 아래에서 선택해 주세요!")
    mbti_type = st.selectbox("🧬 MBTI 유형 선택", options=list(mbti_jobs.keys()))
    if mbti_type:
        st.markdown(f"### 💖 {mbti_type} 유형에게 어울리는 직업은?")
        st.success("✨ " + " | ".join(mbti_jobs[mbti_type]))
        st.markdown("---")
        st.markdown("💡 직업은 MBTI 성격 유형의 일반적인 특성과 연관 지어 추천됩니다. 자신에게 맞는 길을 탐색해보세요! 🚀")

elif selected == "앱 소개":
    st.title("앱 소개 🌟")
    st.markdown("""
    이 웹앱은 MBTI 성격 유형을 기반으로 적절한 직업을 추천하는 **진로 탐색 도우미**입니다.  
    🌻 학생, 취업 준비생, 직무 탐색 중인 모든 분들을 위한 앱이에요!

    - 🧠 MBTI 이론 기반 직업 추천
    - 🎯 맞춤형 커리어 아이디어 제시
    - 🌐 교육 현장에서의 활용 가능

    👉 **"MBTI로 직업 찾기"** 메뉴에서 시작해보세요!
    """)

elif selected == "문의하기":
    st.title("📮 문의하기")
    st.markdown("앱에 대한 피드백이나 개선 제안이 있다면 아래 메일로 보내주세요 ✉")
    st.info("📧 contact@yourdomain.com")
    st.text("💻 제작자: @당신의이름")
