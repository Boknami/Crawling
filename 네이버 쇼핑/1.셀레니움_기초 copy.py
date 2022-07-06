from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

search.send_keys('강아지 사료')
search.send_keys(Keys.ENTER)

