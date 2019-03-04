from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import functions
import time
driver = webdriver.Chrome('./chromedriver')
f =functions.function(driver)

#statistic
kakao_id = 'xygene01@nate.com'
kakao_pw = 'js**91^^11'
naver_id = 'jijohn01'
naver_pw = 'js**91^^1119'
author_name = '김인겸_인큐브랜드'
#variable
contents_cnt = 0
scroll_y = 350
foems = []


#네이버 로그인 접근 후 아이디 비번은 수동으로 입력하여 로그인 해야함
f.naver_go2_login()
wait = WebDriverWait(driver,20)
blog = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='PM_ID_ct']/div[1]/div[2]/div[1]/ul[1]/li[3]/a")))
blog.click()

driver.execute_script("window.open('');")
f.kakao_tap_change()
f.kakao_go2_login(kakao_id,kakao_pw)

driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[text()='"+author_name+"'][1]").click()
driver.implicitly_wait(10)
for five_contents_idx in range (1,10):
    cnt = driver.find_elements_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div")
    for contents_cnt in range(1,len(cnt)+1):

        # 스크롤
        scroll_y = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div[" + str(five_contents_idx) + "]/div/div/div[" + str(contents_cnt) + "]").location
        driver.execute_script("window.scrollTo(0," + str(scroll_y['y']) + ")")

        driver.implicitly_wait(10)
        f.click_more(five_contents_idx,contents_cnt)
        #text 가져오기
        foem = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[4]/div[1]/div").text

        #시 인지 판별 아니면 다음글로
        if not f.is_foem(foem):
            continue
        f.naver_tap_change()
        f.naver_go2_blog_write()
        f.kakao_tap_change()
        print('#####################\n묶음 {} 번째, {}번째글\n'.format(five_contents_idx,contents_cnt))
        foems.append(foem)
        print(foem)
