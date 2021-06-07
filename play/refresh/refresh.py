from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기
import time
import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://analytics.google.com/analytics/web/?authuser=3#/a172003661w239231493p223819001/admin")

while(1):
    time.sleep(1200)
    driver.refresh()
