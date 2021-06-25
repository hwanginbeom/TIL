import time
from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기
import time
import os
from PIL import Image
from selenium.webdriver.chrome.options import Options


# 접속할 웹 사이트 주소
url_list = [
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/aacd189f-cff5-4dbc-a9b3-731c86b1eccd/ReportSection838f50186e0c8eeec289',
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/aacd189f-cff5-4dbc-a9b3-731c86b1eccd/ReportSectionebe4398e6ad094d34d95',
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/aacd189f-cff5-4dbc-a9b3-731c86b1eccd/ReportSectione369ca44a21e77e10763',
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/aacd189f-cff5-4dbc-a9b3-731c86b1eccd/ReportSection7f54f075ced52a2ed6da',
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/aacd189f-cff5-4dbc-a9b3-731c86b1eccd/ReportSectiona6003e3cc8db0a49ab99',
'https://app.powerbi.com/groups/me/apps/229bb21b-608b-4572-9f3b-4f8e229684a1/reports/1d9da6b7-2e70-4bb4-9cdc-9c29cc64c41a/ReportSection7593ca477e39caedb09a'
]

# 캡처 한 사진을 저장할 파일명
title_list = [
"110_1-1.요약.png",
"110_1-2.기간비교.png",
"110_1-3.카테고리 별 검색트렌드.png",
"110_1-4.브랜드 별 검색트랜드.png",
"110_1-9.네이버 검색 키워드 현황.png",
"110_캠페인 orverview.png",
"120_네이버 연관검색어 트랜드.png"
]


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://app.powerbi.com/?route=groups%2fme%2fapps%2f73511425-63b1-43c7-8e77-3cd09764bd17%2freports%2ff2da154f-8158-4327-851c-f607a97c1a89%2fReportSectionc6962d348acaad7aff69&noSignUpCheck=1&pbi_source=weblandingsignin")
time.sleep(2)
driver.find_element_by_name('loginfmt').send_keys('boost@fnfcorp.com')  # 아이디 입력
print("아이디 입력중~")
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_name('passwd').send_keys('dlsqja5511!')  # 비밀번호 입력
print("비밀번호 입력중~!")
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
print("로그인 중 .....")
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)

for i in range(0, len(url_list)):
    print("####################################################")
    print(title_list[i] + " 이미지 캡처중!")
    driver.maximize_window()
    driver.get(url_list[i])
    time.sleep(15)
    ele = driver.find_element_by_class_name('visualContainerHost')
    # total_height = ele.size["height"]+500
    # driver.set_window_size(1920, total_height)  # 전체사이즈로 캡처
    driver.set_window_size(3500, 3000)  # 적당한 사이즈로 캡처
    # driver.set_window_size(2500, 3000)  # 적당한 사이즈로 캡처

    driver.save_screenshot('./dashboard/100/'+title_list[i])

    print(title_list[i] + " 완료!")
    print("####################################################")

    # break
else:
    print('끄읏~')
driver.close()
driver.quit()
