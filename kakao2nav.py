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
scroll_y = 350
foems = []

f.go2kakao_login(kakao_id,kakao_pw)

driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[text()='"+author_name+"'][1]").click()

driver.implicitly_wait(10)
for five_contents_idx in range (1,10):
    cnt = driver.find_elements_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div")
    for contents_cnt in range(1,len(cnt)+1):

        # 스크롤
        scroll_y = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div[" + str(five_contents_idx) + "]/div/div/div[" + str(contents_cnt) + "]").location
        driver.execute_script("window.scrollTo(0," + str(scroll_y) + ")")

        #더보기 클릭
        if driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[4]/p[@class='more _moreBtnContainer']").is_displayed():
            driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div[" + str(five_contents_idx) + "]/div/div/div[" + str(contents_cnt) + "]/div[1]/div[4]/p[@class='more _moreBtnContainer']/a").click()
        #text 가져오기
        foem = driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[4]/div[1]/div").text

        #시 인지 판별
        if foem[0:3]=='[시]':
            print('#####################\n묶음 {} 번째, {}번째글\n'.format(five_contents_idx,contents_cnt))
            foems.append(foem)
            print(foem)
