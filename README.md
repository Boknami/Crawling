Start : 220705
End : 220706

---

# ⭐request

- HTTP통신을 위한 라이브러리(프로그램 개발을 쉽게 해주는 도구)
    
    #인터넷에 접속할 때 서버와 내가 소통하는 HTTP 통신!
    
    - GET요청 = 네이버 기사 1페이지 보여줘
    - POST요청 = 특정 정보들과 함께 (로그인 같은..)
    
- 설치
    - pip install requests

### Code : 네이버 HTML 가져오기

```python
import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)
```

---

# ⭐beautifulsoup

- html 분석을 위한 파이썬 라이브러리

### Code

```python
from bs4 import BeautifulSoup

#Beautifulsoup
soup = BeautifulSoup(html_naver, 'html.parser')

#Beautifulsoup에서 원하는 태그 가져오기
#css선택자를 맨 앞에 붙여주기!
word = soup.select_one('#NM_set_home_btn')

```

---

# ⭐뉴스 제목과 링크 가져오기

1. f12를 사용해서 원하는 부분쪽 구성 확인
2. 예를 들어 뉴스 제목과 링크라면 a 태그 안에서 제목 부분과 href
3. 특정하게 찾을 수 있는 id나 class로 찾기

```python
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

#숙제 : 원하는 키워드로 검색진행하기
keyword = input("키워드 : ")

#서버 요청 + 정보 가져오기
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword)
html_news = response.text

soup = BeautifulSoup(html_news, 'html.parser')
links = soup.select(".news_tit")

num = 1
for link in links:
    title = link.text   #태그 안에 텍스트 가져오기
    url = link.attrs['href'] # href의 속성 가져오기
    print(num,title, url)
    num = num + 1
```

---

# ⭐ URL

- 인터넷 주소 형식

![](https://velog.velcdn.com/images/shin75492/post/89bd5d16-1fe4-4ea2-8912-87734568eb71/image.PNG)
#### 
# ⭐pyautogui

- 마우스, 키보드 매크로 라이브러리

```python
#원하는 키워드로 검색진행하기
keyword = pyautogui.prompt("검색어 입력")
```

---

# ⭐페이지 넘어가며 크롤링

- 페이지를 넘어가면서 URL이 어떻게 변화하는지 살펴본다.

### for문 이용!

```python
for i in range(시작, 끝, 단계)
```

---

# ⭐엑셀과 연동

- openpyxl

```python
import openpyxl

# 1)엑셀 만들기
wb = openpyxl.Workbook()

# 2)엑셀 워크시트 만들기
ws = wb.create_sheet('Test1')

# 3)데이터 추가
ws['A1'] = '순서'
ws['A2'] = '1'

# 4)엑셀 저장
wb.save(r'C:\Users\shin7\OneDrive\바탕 화면\Crawling\엑셀 다루기\강아지_data.xlsx')
```

---

# ⭐셀레니움 사용

- 동작 페이지 ⇒ 단순 request로는 어려워..
- 크롬 드라이버와 연동을 통해 크롬 자동화 동작 수행

♦ find element (s)

html에 존재하는 요소들을 가져온다.

가져온 요소에 + click을 해서 클릭 동작까지 수행이 가능!

♦ 검색창에 글 넣기

1. find element로 가져온 후 click을 해두고.
2. send.key를 이용하여 내용 입력
3. send.key를 이용하여 엔터

```python
search = browser.find_element(By.CLASS_NAME, '_searchInput_search_input_QXUFf')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)
```

♦ 동적 사이트 자동 스크롤

while문 + javascript