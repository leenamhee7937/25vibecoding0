import streamlit as st

# MBTI 타입별 간단 설명 딕셔너리
MBTI_DESCRIPTIONS = {
    "ISTJ": "현실적이고 책임감 있는 관리자 유형",
    "ISFJ": "온정적이고 세심한 수호자 유형",
    "INFJ": "통찰력 있고 이상주의적인 옹호자 유형",
    "INTJ": "전략적이고 독립적인 건축가 유형",
    "ISTP": "논리적이고 융통성 있는 장인 유형",
    "ISFP": "자유로운 영혼의 예술가 유형",
    "INFP": "이상과 가치를 중시하는 중재자 유형",
    "INTP": "분석적이고 혁신적인 사색가 유형",
    "ESTP": "활동적이고 현실적인 촉진자 유형",
    "ESFP": "친근하고 생기 넘치는 연예인 유형",
    "ENFP": "창의적이고 열정적인 활동가 유형",
    "ENTP": "영리하고 논쟁을 즐기는 발명가 유형",
    "ESTJ": "조직적이고 실용적인 집행자 유형",
    "ESFJ": "사교적이고 배려 깊은 제공자 유형",
    "ENFJ": "카리스마 있고 따뜻한 지도자 유형",
    "ENTJ": "결단력 있고 목표 지향적인 지휘관 유형",
}

# 타입 별 궁합 정보
COMPATIBILITY = {
    ("INTJ", "ENFP"): {
        "강점": "창의적 아이디어와 전략적 계획력의 시너지",
        "갈등": "감정 표현 방식 차이로 인한 오해",
        "소통 팁": "서로의 의도와 기대를 명확히 말로 전달하세요."
    },
    ("INFJ", "ESTP"): {
        "강점": "이상주의 vs 현실적 실행력의 균형",
        "갈등": "의사결정 속도 차이로 인한 답답함",
        "소통 팁": "중요 사항은 사전 조율 후 실행하세요."
    },
}

# MBTI별 야식 추천
SNACKS = {
    "ISTJ": ["견과류와 다크초콜릿", "그릭 요거트 파르페", "호두과자"],
    "ISFJ": ["허니브레드", "과일 샐러드", "따뜻한 우유"],
    "INFJ": ["아보카도 토스트", "베리 스무디", "시나몬 롤"],
    "INTJ": ["프로틴바", "블랙커피", "채소스틱"],
    "ISTP": ["팝콘", "감자튀김", "치즈볼"],
    "ISFP": ["아이스크림", "초코칩 쿠키", "밀크티"],
    "INFP": ["치즈케이크", "허브티", "초콜릿 트러플"],
    "INTP": ["라면 컵", "견과류 믹스", "아메리카노"],
    "ESTP": ["치킨 너겟", "피자 롤", "콜라 한 잔"],
    "ESFP": ["와플", "프루트 펀치", "솜사탕"],
    "ENFP": ["핑거 샌드위치", "레모네이드", "팬케이크"],
    "ENTP": ["나쵸", "옥수수칩", "소다"],
    "ESTJ": ["베이글과 크림치즈", "아메리카노", "감자칩"],
    "ESFJ": ["마카롱", "딸기 밀크쉐이크", "치즈스틱"],
    "ENFJ": ["허니버터칩", "요거트 스무디", "허브쿠키"],
    "ENTJ": ["스테이크 조각", "레드 와인", "다크 초콜릿"],
}

# helper function

def get_compatibility(t1, t2):
    pair = (t1, t2)
    if pair in COMPATIBILITY:
        return COMPATIBILITY[pair]
    reverse = (t2, t1)
    if reverse in COMPATIBILITY:
        return COMPATIBILITY[reverse]
    return {
        "강점": "서로의 차이를 배우며 성장할 수 있는 기회",
        "갈등": "서로의 선호와 속도를 이해하는 과정이 필요",
        "소통 팁": "서로의 스타일에 대해 긍정적 피드백을 자주 나누세요."
    }

# Streamlit: 멀티페이지 구조 구현
st.set_page_config(page_title="MBTI Explorer", page_icon="🧭", layout="wide")
page = st.sidebar.selectbox("페이지 선택", ["궁합 & 소통 팁", "MBTI별 야식 추천"])

if page == "궁합 & 소통 팁":
    st.title("💬 MBTI 궁합 & 소통 팁 매칭")
    st.sidebar.header("MBTI 유형 선택")
    type1 = st.sidebar.selectbox("첫 번째 유형", list(MBTI_DESCRIPTIONS.keys()), index=0)
    type2 = st.sidebar.selectbox("두 번째 유형", list(MBTI_DESCRIPTIONS.keys()), index=1)
    info = get_compatibility(type1, type2)
    st.subheader(f"{type1} vs {type2} 궁합 분석")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🌟 강점")
        st.write(info["강점"])
    with col2:
        st.markdown("### ⚠️ 갈등 포인트")
        st.write(info["갈등"])
    with col3:
        st.markdown("### 💡 소통 팁")
        st.write(info["소통 팁"])
    st.markdown("---")
    st.header("개별 유형 기본 설명")
    col4, col5 = st.columns(2)
    with col4:
        st.markdown(f"**{type1}**")
        st.write(MBTI_DESCRIPTIONS[type1])
    with col5:
        st.markdown(f"**{type2}**")
        st.write(MBTI_DESCRIPTIONS[type2])

elif page == "MBTI별 야식 추천":
    st.title("🍽️ MBTI별 야식 추천")
    mbti = st.selectbox("내 MBTI를 선택하세요", list(MBTI_DESCRIPTIONS.keys()))
    st.subheader(f"{mbti}를 위한 오늘의 추천 야식")
    snacks = SNACKS.get(mbti, [])
    if snacks:
        for item in snacks:
            st.write(f"- {item}")
    else:
        st.write("추천 야식 정보를 준비 중입니다.")

# 공통 푸터
st.markdown("---")
st.caption("이 앱은 Streamlit으로 제작되었으며, MBTI 기반 탐색 기능을 제공합니다.")
