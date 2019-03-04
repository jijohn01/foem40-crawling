
class function:
    def __init__(self,driver):
        self.driver = driver
    def kakao_go2_login(self,kakao_id,kakao_pw):
        self.driver.get('https://accounts.kakao.com/login/kakaostory')

        self.driver.find_element_by_id("loginEmail").send_keys(kakao_id)
        self.driver.find_element_by_id("loginPw").send_keys(kakao_pw)
        self.driver.find_element_by_xpath("//*[@id='login-form']/fieldset/button").click()
    def click_more(self,five_contents_idx,contents_cnt):
        if self.driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div["+str(five_contents_idx)+"]/div/div/div["+str(contents_cnt)+"]/div[1]/div[4]/p[@class='more _moreBtnContainer']").is_displayed():
            self.driver.find_element_by_xpath("//*[@id='myStoryContentWrap']/div[2]/div/div/div[1]/div[" + str(five_contents_idx) + "]/div/div/div[" + str(contents_cnt) + "]/div[1]/div[4]/p[@class='more _moreBtnContainer']/a").click()
    def is_foem(self,foem):
        if foem[0:3] == '[시]':
            return True
        return False
    def naver_go2_login(self):
        self.driver.get('https://naver.com')

        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()

    def naver_go2_blog_write(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get("https://blog.naver.com/jijohn01?Redirect=Write")


    def naver_tap_change(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def kakao_tap_change(self):
        self.driver.switch_to.window(self.driver.window_handles[1])