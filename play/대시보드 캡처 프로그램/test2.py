import time
from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기
import time
import os
from PIL import Image
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://app.powerbi.com/?route=groups%2fme%2fapps%2f73511425-63b1-43c7-8e77-3cd09764bd17%2freports%2ff2da154f-8158-4327-851c-f607a97c1a89%2fReportSectionc6962d348acaad7aff69&noSignUpCheck=1&pbi_source=weblandingsignin")
time.sleep(2)
driver.find_element_by_name('loginfmt').send_keys('boost@fnfcorp.com')  # 아이디 입력
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_name('passwd').send_keys('dlsqja5511!')  # 비밀번호 입력
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_id('idSIButton9').click()
driver.maximize_window()
time.sleep(2)




ele = driver.find_element_by_class_name('visualContainerHost')
total_height = ele.size["height"] + 1000

print(ele)
viewport_height = driver.execute_script("return window.innerHeight")
print(viewport_height)
total_height = ele.size["height"] + 1000
driver.set_window_size(1920, total_height)  # the trick
print(""+total_height)
print(total_height)