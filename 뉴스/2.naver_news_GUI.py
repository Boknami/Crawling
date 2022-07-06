import requests
from bs4 import BeautifulSoup
import pyautogui

#원하는 키워드로 검색진행하기
keyword = pyautogui.prompt("검색어 입력")

num = 1
pageNum=1
lastpage = int(pyautogui.prompt("마지막 페이지 입력"))

for page in range(1, lastpage*10 , 10):
    print(f"============================={pageNum}페이지==============================")

    #서버 요청 + 정보 가져오기
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={page}")
    html_news = response.text

    soup = BeautifulSoup(html_news, 'html.parser')
    links = soup.select(".news_tit")


    for link in links:
        title = link.text   #태그 안에 텍스트 가져오기
        url = link.attrs['href'] # href의 속성 가져오기
        print(num,title, url)
        num = num + 1
    pageNum = pageNum+1
