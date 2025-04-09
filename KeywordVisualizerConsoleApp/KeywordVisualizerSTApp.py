import streamlit as st
import pandas as pd
from lib.naverNewsCrawler import searchNaverNews
from lib.myTextMining import process_text
from lib.STVisualizer import visualize_barchart, visualize_wordcloud

st.title("키워드 뉴스 분석기")

# 검색어 키워드 입력
keyword = st.text_input("검색어를 입력하세요:", "")

if st.button("검색 실행"):
    results = searchNaverNews(keyword, 1, 50)
    df = pd.DataFrame(results)
    st.write(df.head())

    word_freq = process_text(results)
    visualize_barchart(word_freq)
    visualize_wordcloud(word_freq)

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    word_freq = process_text(df["content"])
    visualize_barchart(word_freq)
    visualize_wordcloud(word_freq)