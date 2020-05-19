from selenium import webdriver
from secrets import *
from selenium.webdriver.chrome.options import Options
import schedule
from time import sleep

join_time = "17:41"
leave_time = "18:54"

class MeetBot():
    def __init__(self):
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_argument("use-fake-device-for-media-stream")
        option.add_argument("use-fake-ui-for-media-stream") 

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })

        self.driver = webdriver.Chrome(chrome_options=option)


    def login(self):
        self.driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(email)
        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        next_btn.click()
        sleep(1)
        pass_in = self.driver.find_element_by_name('password')
        pass_in.send_keys(password)
        next_pw_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span')
        next_pw_btn.click()


    # not used if micophone and camera are enabled
    def close_popup(self):
        close_popup = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div[3]/div/span/span')
        close_popup.click()

    
    def go_to_meet(self, meet_link):
        self.driver.get(meet_link)
        sleep(2)
        mute_btn = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[1]/div[4]/div[1]/div/div/div')
        mute_btn.click()
        video_btn = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[1]/div[4]/div[2]/div/div')
        video_btn.click()


    def join_meet(self):
        join_btn = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
        join_btn.click()


    # not needed as when its time to leave the browser is stopped
    def leave_meet(self):
        leave_btn = self.driver.find_element_by_xpath('//*[@id="ow4"]/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div')
        leave_btn.click()


if __name__ == '__main__':
    bot = MeetBot()
    bot.login()
    sleep(5)
    bot.go_to_meet(meet)
    schedule.every().day.at(join_time).do(bot.join_meet)
    schedule.every().day.at(leave_time).do(bot.driver.quit)
    while True:
        schedule.run_pending()
        sleep(1)
