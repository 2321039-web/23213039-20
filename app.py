import streamlit as st
import pandas as pd
from konlpy.tag import Okt

# 페이지 설정
st.set_page_config(page_title="아동 어휘 분석기", page_icon="🍎")

@st.cache_resource
def get_okt():
    return Okt()

def main():
    st.title("🍎 아동 어휘 수준 분석기")
    st.write("단어를 입력하면 분석 결과와 연습 문장을 생성합니다.")

    okt = get_okt()
    word = st.text_input("분석할 단어를 입력하세요:", placeholder="예: 학교")

    if word:
        # 형태소 분석
        pos = okt.pos(word)
        
        st.subheader("📊 분석 결과")
        st.write(f"'**{word}**'는 초등 수준의 어휘입니다.")
        
        # 상세 정보 표
        df = pd.DataFrame(pos, columns=['단어', '품사'])
        st.table(df)

        st.subheader("📝 연습용 문장")
        st.info(f"1. 오늘은 {word}에 가서 친구들과 재미있게 놀았어요.")
        st.info(f"2. 선생님께서 {word}에서 지켜야 할 규칙을 알려주셨어요.")

if __name__ == '__main__':
    main()
