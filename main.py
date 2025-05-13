import streamlit as st
from streamlit_option_menu import option_menu

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌈", layout="centered")

# 🎉 상단 메뉴
with st.sidebar:
    selected = option_menu(
        "✨ 탐색 메뉴",
        ["MBTI로 직업 찾기", "앱 소개", "문의하기"],
        icons=["stars", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f9f9f9"},
            "icon": {"color": "#eb4d4b", "font-size": "25px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#f1c40f"},
        },
    )

# 🧠 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🔬 과학자", "📊 전략 컨설턴트", "💻 데이터 과학자"],
    "INTP": ["🧪 연구원", "🎮 게임 디자이너", "📚 이론 물리학자"],
    "ENTJ": ["💼 CEO", "📈 경영 컨설턴트", "🏛 정책 분석가"],
    "ENTP": ["📢 마케팅 전문가", "💡 창업가", "🧠 발명가"],
    "INFJ": ["🧑‍🏫 교사", "💬 심리상담사", "🎨 예술가"],
    "INFP": ["📖 작가", "🎼 작곡가", "🌿 환경 운동가"],
    "ENFJ": ["🎤 연설가", "👥 HR 전문가", "🎭 연극 연출가"],
    "ENFP": ["🎙 방송인", "✈ 여행 작가", "🎨 크리에이터"],
    "ISTJ": ["⚖ 판사", "📊 회계사", "🧑‍💻 시스템 관리자"],
    "ISFJ": ["🧑‍⚕ 간호사", "🏫 초등교사", "📦 물류 관리자"],
    "ESTJ": ["🏗 프로젝트 매니저", "📋 관리자", "💰 금융 분석가"],
    "ESFJ": ["👩‍🏫 상담교사", "🏥 병원 행정가", "🛍 판매 관리자"],
    "ISTP": ["🛠 기술자", "🏍 레이서", "🔧 정비사"],
    "ISFP": ["🎨 그래픽 디자이너", "📷 사진작가", "🌸 플로리스트"],
    "ESTP": ["🚓 경찰", "💼 세일즈 매니저", "🎤 MC"],
    "ESFP": ["🎬 배우", "🕺 댄서", "🎤 가수"],
}

# ✨ 직업 추천 메인 화면
if selected == "MBTI로 직업 찾기":
    st.markdown("<h1 style='text-align: center; color: #e67e22;'>🌈 MBTI로 알아보는 나의 진로 ✨</h1>", unsafe_allow_html=True)
    st.markdown("#### 당신의 MBTI는 무엇인가요? 😍 아래에서 선택해 주세요!")

    mbti_type = st.selectbox("🧬 MBTI 유형 선택", options=mbti_jobs.keys())

    if mbti_type:
        st.markdown(f"### 💖 {mbti_type} 유형에게 어울리는 직업은?")
        st.success("✨ " + " | ".join(mbti_jobs[mbti_type]))
        st.markdown("---")
        st.markdown("💡 직업은 MBTI 성격 유형의 일반적인 특성과 연관 지어 추천됩니다. 자신에게 맞는 길을 탐색해보세요! 🚀")

# 📘 앱 소개
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

# 📬 문의하기
elif selected == "문의하기":
    st.title("📮 문의하기")
    st.markdown("앱에 대한 피드백이나 개선 제안이 있다면 아래 메일로 보내주세요 ✉")
    st.info("📧 contact@yourdomain.com")
    st.text("💻 제작자: @당신의이름")

