import requests
from bs4 import BeautifulSoup

#요청 보내고 response로 응답 받기
response = requests.get("https://www.naver.com")

#받은 정보에서 html 정보를 html에 저장
html_naver = response.text

#Beautifulsoup
soup = BeautifulSoup(html_naver, 'html.parser')

#Beautifulsoup에서 원하는 태그 가져오기
#css선택자를 맨 앞에 붙여주기!
word = soup.select_one('#NM_set_home_btn')

print(word.text)