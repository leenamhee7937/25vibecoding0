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
    # 기본 케이스: 모든 조합에 대해 비슷한 구조로 제공
}

# 사용자 정의 함수: 조합 키 생성 및 정보 반환

def get_compatibility(t1, t2):
    if (t1, t2) in COMPATIBILITY:
        return COMPATIBILITY[(t1, t2)]
    if (t2, t1) in COMPATIBILITY:
        return COMPATIBILITY[(t2, t1)]
    return {
        "강점": "서로의 차이를 배우며 성장할 수 있는 기회",
        "갈등": "서로의 선호와 속도를 이해하는 과정이 필요",
        "소통 팁": "서로의 스타일에 대해 긍정적 피드백을 자주 나누세요."
    }

# Streamlit 앱 구성
st.set_page_config(page_title="MBTI 궁합 & 소통 팁", page_icon="💬", layout="wide")
st.title("💬 MBTI 궁합 & 소통 팁 매칭")

# 사이드바에서 두 가지 MBTI 타입 선택
st.sidebar.header("MBTI 유형 선택")
type1 = st.sidebar.selectbox("첫 번째 유형", list(MBTI_DESCRIPTIONS.keys()), index=0)
type2 = st.sidebar.selectbox("두 번째 유형", list(MBTI_DESCRIPTIONS.keys()), index=1)

# 선택된 유형 설명
st.subheader(f"{type1} vs {type2} 궁합 분석")
info = get_compatibility(type1, type2)

# 세 가지 주요 정보 표시
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

# 추가 섹션: 개별 타입 설명
st.markdown("---")
st.header("개별 유형 기본 설명")
col4, col5 = st.columns(2)
with col4:
    st.markdown(f"**{type1}**")
    st.write(MBTI_DESCRIPTIONS[type1])
with col5:
    st.markdown(f"**{type2}**")
    st.write(MBTI_DESCRIPTIONS[type2])

# 하단 푸터
st.markdown("---")
st.caption("이 앱은 Streamlit으로 제작되었으며, MBTI 기반의 궁합 및 소통 팁을 제공합니다.")
