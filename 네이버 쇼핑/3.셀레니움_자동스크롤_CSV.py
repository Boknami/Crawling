from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(1) #로딩 대기

# 쇼핑 메뉴 열기
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(1)

# 검색창 클릭
search = browser.find_element(By.CLASS_NAME, '_searchInput_search_input_QXUFf')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이 저장
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 자동 스크롤 : 맨 아래까지 스크롤
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 부하 방지 : 로딩 시간 추가
    time.sleep(1)

    # 높이 체크 : 스크롤 후
    after_h = browser.execute_script("return window.scrollY")

    # 오류 방지 : 스크롤을 내렸는데도 처음과 동일하다
    if after_h == before_h:
        break

    before_h = after_h

# 파일 생성
f = open(r"C:\Users\shin7\OneDrive\바탕 화면\Crawling\네이버 쇼핑\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".basicList_title__3P9Q7").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__2WUXn").text
    except:
        price = "판매중단"
    
    link = item.find_element(By.CSS_SELECTOR, ".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price)
    print(link)
    csvWriter.writerow([name, price, link])
    print('============================================')

# 파일 닫기
f.close()
