from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import functions
import time


driver = webdriver.Chrome('./chromedriver')
action = webdriver.common.action_chains.ActionChains(driver)

f =functions.function(driver)

#statistic
kakao_id = 'xygene01@nate.com'
kakao_pw = 'js**91^^11'
naver_id = 'jijohn01'
naver_pw = 'js**91^^1119'
author_name = '김인겸_인큐브랜드'
foem_per_day = 144
foem_cnt = 0
#variable
contents_cnt = 0
scroll_y = 350
foems = []


#네이버 로그인 접근 후 아이디 비번은 수동으로 입력하여 로그인 해야함
f.naver_go2_login()
wait = WebDriverWait(driver,20)
blog = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='PM_ID_ct']/div[1]/div[2]/div[1]/ul[1]/li[3]/a")))
blog.click()
f.naver_go2_blog_write()

driver.switch_to.frame("mainFrame")
if driver.find_element_by_xpath("//*[@id='blog-editor']/div/div/div/div[1]/article/div/header/button").is_displayed():
    driver.find_element_by_xpath("//*[@id='blog-editor']/div/div/div/div[1]/article/div/header/button").click()
driver.switch_to.default_content()

driver.execute_script("window.open('');")
f.kakao_tap_change()
f.kakao_go2_login(kakao_id,kakao_pw)

driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[text()='"+author_name+"'][1]").click()
driver.implicitly_wait(10)
for five_contents_idx in range (1,1000):
    if foem_cnt >= foem_per_day:
        break
    cnt = driver.find_elements_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div")
    for contents_cnt in range(1,len(cnt)+1):

        # 스크롤
        scroll_y = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div[" + str(five_contents_idx) + "]/div/div/div[" + str(contents_cnt) + "]").location
        driver.execute_script("window.scrollTo(0," + str(scroll_y['y']-100) + ")")

        driver.implicitly_wait(10)
        if 't:remove'==driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[3]/div[@class='btn_top_group']/div/div/a").get_attribute('data-kant-option'):
            continue
        time.sleep(0.5)

        f.click_more(five_contents_idx,contents_cnt)
        #text 가져오기
        foem = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[4]/div[1]/div").text

        #시 인지 판별 아니면 다음글로
        if not f.is_foem(foem):
            continue
        f.naver_tap_change()
        f.naver_go2_blog_write()
        foem_cnt +=1

        f.naver_blog_write(foem)
        f.kakao_tap_change()
        print('#####################\n묶음 {} 번째, {}번째글\n'.format(five_contents_idx,contents_cnt))
        print(foem+'\n Count:{}'.format(foem_cnt))
        driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[3]/div[@class='btn_top_group']/div/div").click()
        if foem_cnt >= foem_per_day:
            break

driver.close()