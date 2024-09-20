import requests, json
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# 參數資訊
url = "https://www.google.com/advanced_image_search"
send_key_1 = "登山 遊記"  # 含有以下所有字詞
send_key_2 = "youtube"   # 不含以下任何字詞
locator = (By.CLASS_NAME, 'jYcx0e')

# 啟動瀏覽器工具的選項
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--lang=zh-TW")
options.add_argument("--disable-popup-blocking")

# 使用ChromeDriverManager自動下載對應版本chromedriver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path), options=options)
driver.get(url)

# 開始爬取
inputElement = driver.find_element(By.ID, 'xX4UFf')
inputElement.send_keys(send_key_1)
inputElement = driver.find_element(By.ID, 't2dX1c')
inputElement.send_keys(send_key_2)
to_element = driver.find_element(By.ID, 'cr_button')   # 地區
countryTW = driver.find_element(By.ID, ':v')
action_chains = ActionChains(driver).move_to_element(to_element).click().move_to_element(countryTW).click()
action_chains.perform()

try:
    inputElement.submit()

except Exception as e:
    print(e)

sleep(10)