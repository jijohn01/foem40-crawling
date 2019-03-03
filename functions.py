
class function:
    def __init__(self,driver):
        self.driver = driver
    def go2kakao_login(self,kakao_id,kakao_pw):
        self.driver.get('https://accounts.kakao.com/login/kakaostory')

        self.driver.find_element_by_id("loginEmail").send_keys(kakao_id)
        self.driver.find_element_by_id("loginPw").send_keys(kakao_pw)
        self.driver.find_element_by_xpath("//*[@id='login-form']/fieldset/button").click()