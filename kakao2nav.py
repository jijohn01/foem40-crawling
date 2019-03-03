from selenium import webdriver
import functions

driver = webdriver.Chrome('./chromedriver')
f =functions.function(driver)

#statistic
kakao_id = 'xygene01@nate.com'
kakao_pw = 'js**91^^11'
author_name = '김인겸_인큐브랜드'
#variable
contents_cnt = 0

f.go2kakao_login(kakao_id,kakao_pw)

driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[text()='"+author_name+"'][1]").click()

driver.implicitly_wait(10)
for contents_cnt in range(5):
    foem = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[4]/div[1]/div").text
    if foem[0:3]=='[글]':
        print('pass')
    print(foem)
    print(foem[0:3])