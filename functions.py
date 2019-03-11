from pynput.keyboard import Key,Controller
import pyperclip
from selenium import webdriver
import pyautogui
import time

class function:
    def __init__(self,driver):
        self.driver = driver
        self.action = webdriver.common.action_chains.ActionChains(self.driver)
        self.naver_id = "40jasi"
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
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()

    def naver_go2_blog_write(self):
        self.driver.get("https://blog.naver.com/"+self.naver_id+"?Redirect=Write")

    def naver_blog_write(self, foem):
        time.sleep(1)

        self.driver.switch_to.frame("mainFrame")
        pyperclip.copy(foem)

        pyautogui.moveTo(500,900)
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.hotkey('ctrl','v')
        time.sleep(0.5)
        #self.driver.find_element_by_xpath("//div[@class='se-drop-indicator']").send_keys(foem)
        title = self.driver.find_element_by_xpath("//div[@class='se-drop-indicator']/div/div/p[1]/span").text
        pyperclip.copy(title)
        pyautogui.scroll(700)
        time.sleep(0.5)
        pyautogui.click(500,320)
        time.sleep(0.4)
        pyautogui.hotkey('ctrl','v')
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//*[@id='header']/div/div[3]/button").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//*[@id='header']/div/div[3]/div/div[2]/div[2]/div/button").click()
        time.sleep(0.7)
        self.driver.switch_to.default_content()





    def naver_tap_change(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def kakao_tap_change(self):
        self.driver.switch_to.window(self.driver.window_handles[1])