#pip install selenium webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions() #자동으로 다운받은 후 실행
driver = webdriver.Chrome(service=Service(
      ChromeDriverManager().install()),
      options=chrome_options)

ID = 'lhj2442'
PW = 'zheld123'
# \지우고 한줄로 써도 사용 가능
url = 'https://memberssl.auction.co.kr/Authenticate/default.aspx?\
url=http%3A//corners.auction.co.kr/AllKill/AllDay.aspx'
driver.get(url)               #해당 url로 접속
driver.implicitly_wait(3)     #인터넷정보 다 다운받을 때까지 대기(초)

e = driver.find_element(By.ID, 'id')
e.clear()
e.send_keys(ID)
e = driver.find_element(By.ID,'password')
e.clear()
e.send_keys(PW)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(3)     #인터넷정보 다 다운받을 때까지 대기(초)

driver.get('https://escrow.auction.co.kr/close/\
OrderProcessList.aspx?loginType=50')
webpage = driver.page_source

#상품명 출력
products = driver.find_elements(By.CLASS_NAME,'product-name')
for i in products:
      print(i.text)
#주문번호 출력
products = driver.find_elements(By.CLASS_NAME,'product-order-num')
for i in products:
      print(i.text)
#상품금액 출력
products = driver.find_elements(By.CLASS_NAME,'charge')
for i in products:
      print(i.text)
