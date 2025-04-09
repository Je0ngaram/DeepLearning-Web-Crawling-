# Keyword Visualizer Console & Web App

입력한 키워드를 바탕으로 네이버 뉴스의 데이터를 수집하고 텍스트 마이닝과 시각화를 통해서 관련 키워드를 분석해주는 프로젝트이다.
콘솔과 스트림릿 형태로 CSV 파일 저장, 단어 빈도수 막대 그래프, 워드 클라우드 기능이 있다.

# 프로젝트 구조
KeywordVisualizerConsoleApp.py # 콘솔 앱 실행 파일
KeywordVisualizerSTApp.py      # Streamlit 웹 앱 실행 파일
data                           # 수집된 뉴스 데이터 CSV 파일이 저장되는 폴더
myTextMining.py                # 텍스트 전처리 및 분석
naverNewsCrawler.py            # 네이버 뉴스 크롤링
STVisualizer.py                # 시각화 (단어 빈도수 막대 그래프, 워드 클라우드)

# <주요 기능>
# 1. 키워드 기반 네이버 뉴스 수집
- 한글 키워드 입력 -> 네이버 뉴스의 검색 결과 수집
- CSV 파일로 저장 가능함(저장의 여부를 선택할 수 있음)

# 2. 텍스트 마이닝
- 뉴스 제목 텍스트에서 불용어 제거 및 명사를 추출함
- 단어 빈도 분석

# 3. 시각화
- 단어 빈도수 막대 그래프
- 워드 클라우드

# 4. 실행 환경
- 콘솔 앱: `KeywordVisualizerConsoleApp.py`
- 웹 앱: `KeywordVisualizerSTApp.py` (스트림릿 기반)