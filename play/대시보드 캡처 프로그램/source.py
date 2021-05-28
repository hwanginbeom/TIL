import time
from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기



url = 'https://app.powerbi.com/?route=groups%2fme%2fapps%2f73511425-63b1-43c7-8e77-3cd09764bd17%2freports%2ff2da154f-8158-4327-851c-f607a97c1a89%2fReportSectionc6962d348acaad7aff69&noSignUpCheck=1&pbi_source=weblandingsignin'        # 접속할 웹 사이트 주소 (네이버)
driver = webdriver.Chrome('chromedriver.exe')  # 크롬 드라이버로 크롬 켜기
driver.get(url)
time.sleep(2) 
driver.find_element_by_name('loginfmt').send_keys('boost@fnfcorp.com') # 아이디
driver.find_element_by_id('idSIButton9').click()
time.sleep(2) 
driver.find_element_by_name('passwd').send_keys('dlsqja5511!')  # 비밀번호
driver.find_element_by_id('idSIButton9').click()
time.sleep(2) 
driver.find_element_by_id('idSIButton9').click()
driver.maximize_window()


url = 'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSectionc6962d348acaad7aff69'        # 접속할 웹 사이트 주소 
driver.get(url)
time.sleep(10) 
driver.save_screenshot("./dashboard/610_Overview.png")

url = 'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSectione492dfe5670b92500863'        # 접속할 웹 사이트 주소 (네이버)
driver.get(url)
time.sleep(10) 
driver.save_screenshot("./dashboard/610_타겟팅 결과.png")

url = 'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSection56f31ed4bd34c3029748'        # 접속할 웹 사이트 주소 (네이버)
driver.get(url)
time.sleep(10) 
driver.save_screenshot("./dashboard/610_타겟팅 결과_매장지역.png")

url = 'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSection0c62168315e882971853'        # 접속할 웹 사이트 주소 (네이버)
driver.get(url)
time.sleep(15) 
driver.save_screenshot("./dashboard/610_구매제품 RANK.png")

driver.close()
