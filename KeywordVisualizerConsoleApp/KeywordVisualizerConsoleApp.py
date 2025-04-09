import pandas as pd
import streamlit as st

from lib.naverNewsCrawler import searchNaverNews, saveSearchResult_CSV, setNewsSearchResult
from lib.myTextMining import process_text
from lib.STVisualizer import visualize_barchart, visualize_wordcloud

# 사이드바 - 파일 업로드
st.sidebar.header("파일 선택")
uploaded_file = st.sidebar.file_uploader("파일 업로드", type=["csv"])

# 데이터 초기화
data = None
columns = []
selected_column = None

if uploaded_file is not None:
    # 파일이 업로드되었을 때만 데이터 로드
    data = pd.read_csv(uploaded_file)
    columns = data.columns.tolist()

# 데이터 컬럼 선택
st.sidebar.subheader("데이터 컬럼 선택")
selected_column = st.sidebar.selectbox("데이터가 있는 컬럼명",
                                       columns if columns else ["(파일을 업로드하세요)"])

# 데이터 파일 확인 버튼
if st.sidebar.button("데이터 파일 확인") and data is not None:
    st.subheader("업로드한 데이터")
    st.write(data)

st.sidebar.subheader("설정")
show_bar_chart = st.sidebar.checkbox("빈도수 그래프", value=True)
num_words_bar = st.sidebar.slider("단어 수", min_value=10, max_value=50, value=10, step=1)

show_wordcloud = st.sidebar.checkbox("워드 클라우드", value=True)
num_words_wc = st.sidebar.slider("단어 수", min_value=20, max_value=500, value=50, step=10)

# 분석 시작 버튼
if st.sidebar.button("분석 시작"):
    if data is None:
        st.warning("CSV 파일 업로드")
    else:
        # 선택한 컬럼의 텍스트 데이터 추출
        text_data = " ".join(data[selected_column].astype(str))

        # 텍스트 처리
        word_freq = process_text(text_data)

        # 그래프와 워드클라우드를 나란히 표시
        col1, col2 = st.columns(2)

        if show_bar_chart:
            with col1:
                st.subheader("빈도수 그래프")
                visualize_barchart(word_freq, num_words_bar)

        if show_wordcloud:
            with col2:
                st.subheader("워드 클라우드")
                visualize_wordcloud(word_freq, num_words_wc)
