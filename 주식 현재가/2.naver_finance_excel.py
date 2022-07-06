from cgi import print_arguments
import requests
from bs4 import BeautifulSoup
import openpyxl

f_path = r'C:\Users\shin7\OneDrive\바탕 화면\Crawling\주식 현재가\data.xlsx'

wb = openpyxl.load_workbook(f_path)
ws = wb.active
# 종목 코드 리스트
codes = [
    '005930',
    '071200',
    '035720'
]

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html=response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(f"{price}원")
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(f_path)