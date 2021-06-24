from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기
import time
from selenium.webdriver.chrome.options import Options
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
createFolder('./dashboard/600')


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


# 400번 시작


url_list = [
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSectionc6962d348acaad7aff69' ,
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSectionc54b918c6275a0dccd56',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSectione492dfe5670b92500863',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSection56f31ed4bd34c3029748' ,
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/f2da154f-8158-4327-851c-f607a97c1a89/ReportSection0c62168315e882971853',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSectionf071031e9dc7a435ce74' ,
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSectionf9bd636eda0ec7108fe6'
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSectionf5400782ca8e8eb942b9',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSection9320eeaf41069e081658',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSection2fa930e464c333b22cce',
'https://app.powerbi.com/groups/me/apps/73511425-63b1-43c7-8e77-3cd09764bd17/reports/1f94c6b4-d87a-4f38-970c-489e91292178/ReportSection3d8b43e1a1b3a1b0daa7'
]

# 캡처 한 사진을 저장할 파일명
title_list = [
"610_Overview.png",
"610_detail.png",
"610_타겟팅 결과.png",
"610_타겟팅 결과_매장지역.png",
"610_구매제품 RANK.png",
"620_캠페인 orverview.png",
"620_유입및행동_마케팅유입지표orverview.png",
"620_유입및행동_인기유입지표.png",
"620_ROI.png",
"620_구매고객 분석.png",
"620_Funnel분석.png"
]

print("####################################################")
print("######################600번 시작#####################")
print("####################################################")
for i in range(0, len(url_list)):
    print(title_list[i] + " 이미지 캡처중!")
    driver.maximize_window()
    driver.get(url_list[i])
    time.sleep(15)
    ele = driver.find_element_by_class_name('visualContainerHost')
    driver.set_window_size(3500, 3000)  # 적당한 사이즈로 캡처

    driver.save_screenshot('./dashboard/600/'+title_list[i])

    print(title_list[i] + " 완료!")
    # break
else:
    print('끄읏~')


driver.close()
driver.quit()