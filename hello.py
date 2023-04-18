import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"  # 삼성전자 종목 페이지 URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 현재가 정보 추출
price = soup.select_one("#_nowVal").text
print("현재 주가:", price)
