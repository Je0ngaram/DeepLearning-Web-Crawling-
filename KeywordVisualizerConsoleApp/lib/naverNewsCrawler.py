import os
import urllib.request
import json
import pandas as pd

def searchNaverNews(keyword, start, display):
    client_id = "tcSi69R4floh92_UREPO"
    client_secret = "zgHlqZNJHV"

    # 한글 검색어 안전하게 변환
    encText = urllib.parse.quote(keyword)

    # uri + query 생성
    url = "https://openapi.naver.com/v1/search/news?query=" + encText  # JSON 결과

    # request message 구성
    new_url = url + f"&start={start}&display={display}"
    request = urllib.request.Request(new_url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    resultJSON = None
    try:
        # request -> response 받아오기
        response = urllib.request.urlopen(request)

        # 받아온 결과가 정상인지 확인
        rescode = response.getcode()
        if rescode == 200:
            # 정상이면 데이터 읽어오기
            response_body = response.read()
            # 한글이 있으면 utf-8 decoding
            resultJSON = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code:", rescode)
    except Exception as e:
        print(e)
        print(f"Error : {new_url}")

    return resultJSON

# 응답 데이터를 리스트에 저장 (검색 결과는 JSON의 'items'에 들어 있음)
def setNewsSearchResult(resultAll, resultJSON):
    for result in resultJSON['items']:
        resultAll.append(result)

# JSON 리스트를 DataFrame으로 변환 후 CSV 파일로 저장
def saveSearchResult_CSV(json_list, filename):
    data_df = pd.DataFrame(json_list)
    data_df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"{filename} SAVED")

keyword = input("검색어 : ").strip()

# CSV 저장 여부 선택하는 기능..
save_csv = input("CSV 저장(y/n) : ").strip().lower() == 'y'

# 검색 결과를 저장할 리스트 초기화
resultAll = []

# 첫 검색 API 호출
start = 1
display = 10
resultJSON = searchNaverNews(keyword, start, display)

while (resultJSON is not None) and (resultJSON['display'] > 0):
    # 응답 데이터를 리스트에 저장
    setNewsSearchResult(resultAll, resultJSON)

    # 다음 검색 API 호출을 위한 파라미터 조정
    start += resultJSON['display']

    # API 호출
    resultJSON = searchNaverNews(keyword, start, display)

    # API 호출 성공 여부 출력
    if resultJSON is not None:
        print(f"{keyword} [{start}] : Search Request Success")
    else:
        print(f"{keyword} [{start}] : error...!!!")

# 사용자가 'y'를 입력하면 CSV 파일로 저장
if save_csv:
    filename = f"./data/{keyword}_naver_news.csv"
    saveSearchResult_CSV(resultAll, filename)