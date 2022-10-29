from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, \
    NoSuchElementException
from time import sleep

CHROME_DRIVER_PATH = "C:\Developement\chromedriver.exe"
USERNAME = "automated_python_bot"
PASSWORD = "meat@automated_python_bot"
TARGET_AC = "prathamesh_dol196"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username = self.driver.find_element(By.NAME, "username")  # search username field
        username.click()  # click on username field
        username.send_keys(USERNAME)  # entering username

        password = self.driver.find_element(By.NAME, "password")  # search password field
        password.click()  # click on password field
        password.send_keys(PASSWORD)  # entering password

        password.send_keys(Keys.ENTER)  # hitting enter

        sleep(5)  # sleep until data is loaded

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
        # ^ click on not now on popup of save your login info

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()
        # ^ clicks on second popup

        sleep(3)  # sleep until data is loaded

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_AC}")  # open targeted accounts url
        sleep(5)  # sleep until data is loaded

        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')  # click on followers
        followers.click()

        sleep(2)  # sleep until data is loaded

        modal = self.driver.find_element(By.XPATH, "//div[@Class='isgrP']")  # deals with followers popup window
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")  # getting all follow buttons
        for button in all_buttons:  # looping through all buttons
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

    def unfollow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")  # getting all follow buttons
        for button in all_buttons:
            try:  # looping through all buttons
                if button.text == "Following" or button.text == "Requested":
                    button.click()
            except ElementClickInterceptedException:
                sleep(1)
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[1]')
                cancel_button.click()
                sleep(1)


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()  # this method is used to follow
insta_follower.unfollow()  # this method is used to unfollow
