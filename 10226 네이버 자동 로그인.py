from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time



chrome_options = webdriver.ChromeOptions() #자동으로 다운받은 후 실행
driver = webdriver.Chrome(service=Service(
      ChromeDriverManager().install()),
      options=chrome_options)

ID = 'kanca512'
PW = '0615ab@Blind22'

# \지우고 한줄로 써도 사용 가능
url = 'https://nid.naver.com'
driver.get(url)               #해당 url로 접속
#driver.implicitly_wait(3)     #인터넷정보 다 다운받을 때까지 대기(초)

a = driver.find_element(By.ID,'id')
a.click()
pyperclip.copy(ID)
a.send_keys(Keys.CONTROL,'v')
time.sleep(2)

aa = driver.find_element(By.ID,'pw')
aa.click()
pyperclip.copy(PW)
aa.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

driver.find_element(By.ID,'log.login').click()

time.sleep(2)
driver.get('http://www.naver.com')
