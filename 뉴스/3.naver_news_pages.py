import requests
from bs4 import BeautifulSoup
import pyautogui

#원하는 키워드로 검색진행하기
keyword = pyautogui.prompt("검색어 입력")

#서버 요청 + 정보 가져오기
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html_news = response.text

soup = BeautifulSoup(html_news, 'html.parser')
links = soup.select(".news_tit")

num = 1
for link in links:
    title = link.text   #태그 안에 텍스트 가져오기
    url = link.attrs['href'] # href의 속성 가져오기
    print(num,title, url)
    num = num + 1
