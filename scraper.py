import requests, json
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# 啟動瀏覽器工具的選項
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--disable-popup-blocking")55
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# service = Service(executable_path="./chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
inputElement = driver.find_element(By.ID, 'APjFqb')
inputElement.send_keys("登山 遊記")