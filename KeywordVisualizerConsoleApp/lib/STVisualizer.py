import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
from collections import Counter
from matplotlib import font_manager, rc

st.title("데이터 파일 확인 및 분석")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    data_df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:", data_df.head())

    # 컬럼 선택
    col_options = list(data_df.columns)
    selected_col = st.selectbox("확인할 컬럼 선택", col_options)
    
    if selected_col:
        st.write(f"### 선택한 컬럼: {selected_col}")
        st.dataframe(data_df[[selected_col]].head(), use_container_width=True)
        
        # 탭 생성 (데이터 미리보기 & 빈도수 분석)
        tab1, tab2 = st.tabs(["데이터 미리보기", "빈도수 분석"])
        
        with tab1:
            st.write("선택한 컬럼 데이터 미리보기")
            st.dataframe(data_df[[selected_col]], height=300, use_container_width=True)
        
        with tab2:
            st.write("빈도수 분석 결과")
            word_counts = data_df[selected_col].value_counts().head(20)
            st.bar_chart(word_counts)


# 한글 폰트 설정
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def visualize_barchart(counter, top_n=20, title="단어 빈도수 그래프", xlabel="빈도수", ylabel="단어"):
    most_common = counter.most_common(top_n)
    word_list = [word for word, _ in most_common]
    count_list = [count for _, count in most_common]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(word_list[::-1], count_list[::-1], color='skyblue')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=14)
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    st.pyplot(fig)

def visualize_wordcloud(counter, max_words=50):
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=500,
        max_words=max_words,
        background_color='white',
        colormap='coolwarm'
    ).generate_from_frequencies(counter)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    st.pyplot(fig)