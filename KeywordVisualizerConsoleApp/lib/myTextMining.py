import re
import collections
import matplotlib.pyplot as plt
import streamlit as st

from matplotlib import font_manager, rc
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter

def load_corpus_from_csv(corpus_file, col_name):
    import pandas as pd
    data_df = pd.read_csv(corpus_file)
    result_list = list(data_df[col_name])
    return result_list

def tokenize_korean_corpus(corpus_list, tokenizer, tags, stopwords):
    text_pos_list = []
    for text in corpus_list:
        text_pos = tokenizer(text)
        text_pos_list.extend(text_pos)
    token_list = [token for token, tag in text_pos_list if tag in tags and token not in stopwords]
    return token_list

def analyze_word_freq(corpus_list, tokenizer, tags, stopwords):
    token_list = tokenize_korean_corpus(corpus_list,tokenizer, tags, stopwords)
    counter = Counter(token_list)
    return counter

def process_text(text):
    okt = Okt()
    
    # 특수문자 및 불필요한 문자 제거
    #text = re.sub(r"[^가-힣\s]", "", text)
    # 형태소 분석을 사용해 명사 추출
    words = okt.nouns(text)
    # 단어 빈도 계산
    word_freq = collections.Counter(words)
    return word_freq


def visualize_barchart(counter, title, xlabel, ylabel):
    
    # 한글 폰트 설정하기
    # matplotlib 한글 폰트 설정
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    # 수평 막대그래프
    plt.barh(word_list[::-1], count_list[::-1])

    most_common = counter.most_common(20)
    word_list = [word for word, _ in most_common]
    count_list = [count for _, count in most_common]

    fig, ax = plt.subplots()
    # 가장 많이 나온 단어가 맨 위로 가도록 역순 정렬
    ax.barh(word_list[::-1], count_list[::-1], color='skyblue')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    st.pyplot(fig)

def visualize_wordcloud(counter):

    font_path = "c:/Windows/fonts/malgun.ttf"

    wordcloud = WordCloud(font_path=font_path,
                          width=600,
                          height=400,
                          max_words=50,
                          background_color='ivory').generate_from_frequencies(counter)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis('off')

    st.pyplot(fig)