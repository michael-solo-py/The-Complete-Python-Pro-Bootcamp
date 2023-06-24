from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

DOWNLOAD_SPEED = 50
UPLOAD_SPEED = 28
EMAIL = 'youemail@gmail.com'
PASSWORD = 'youpassword'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.maximize_window()

        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(40)

        wait = WebDriverWait(self.driver, 40)
        self.down = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"))).text

        self.up = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text
        print('DOWN: ' + self.down)
        print('UP: ' + self.up)

        # self.driver.close()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/compose/tweet")
        self.driver.maximize_window()

        time.sleep(5)
        input_email = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        input_email.send_keys(EMAIL)
        input_email.send_keys(Keys.ENTER)

        time.sleep(3)

        unusual_login = self.driver.find_element(By.CSS_SELECTOR, '.r-30o5oe')
        # if unusual_login.get_attribute('data-testid') == 'ocfEnterTextTextInput':
        unusual_login.send_keys('whosher90909')
        unusual_login.send_keys(Keys.ENTER)

        time.sleep(3)

        input_pass = self.driver.find_element(By.CSS_SELECTOR, '.r-homxoj')
        input_pass.send_keys(PASSWORD)
        input_pass.send_keys(Keys.ENTER)

        time.sleep(5)

        write_twit = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_twit.send_keys(f"Hey Internet Provider. Why is my Internet speed is {self.down}down/{self.up}up when I pay for {DOWNLOAD_SPEED}down/{UPLOAD_SPEED}up?")

        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(30)

        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
