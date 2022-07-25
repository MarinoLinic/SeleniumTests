# Install Selenium. I installed it in a virtual PyCharm environment using "pip3 install selenium"
# Install chromedriver so you don't have to mess around with PATH. "pip install chromedriver-autoinstaller"

import chromedriver_autoinstaller

import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os
import random

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# os.environ['PATH'] += r"C:\Users\user\Desktop\Untitled Folder\SeleniumTests\chromedriver_win32"
chromedriver_autoinstaller.install()


def browsers(driver):
    driver.maximize_window()
    driver.get(r"http://sigmachatapp.xyz/app")

    while 1:
        sleep(3)

        connect = driver.find_element(By.CLASS_NAME, "connect")
        connect.click()
        driver.implicitly_wait(5)

        username = driver.find_element(By.ID, "username")
        username.send_keys("Osoba", random.randint(0, 1000000))

        age = driver.find_element(By.ID, "age")
        age.click()
        age.send_keys(Keys.RETURN)
        age.send_keys(Keys.DOWN)
        age.send_keys(Keys.RETURN)

        country = driver.find_element(By.ID, "country")
        country.click()
        country.send_keys(Keys.RETURN)
        country.send_keys(Keys.DOWN)
        country.send_keys(Keys.RETURN)

        about = driver.find_element(By.ID, "about")
        about.send_keys("Hehe")

        sex = driver.find_element(By.XPATH, "//input[@value='Male']")
        sex.click()

        confirm = driver.find_element(By.CLASS_NAME, "swalPopup-confirmButton")
        confirm.click()

        for i in range(0, 30):
            message_box = driver.find_element(By.ID, "message-input-box")
            message_box.click()
            message_box.send_keys("Manjcraft ", random.randint(0, 1000))
            message_box.send_keys(Keys.RETURN)

        driver.refresh()  # the input gets slow after a while, so we'll refresh for efficiency


driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()
driver5 = webdriver.Chrome()

t1 = threading.Thread(target=browsers, args=[driver1])
t2 = threading.Thread(target=browsers, args=[driver2])
t3 = threading.Thread(target=browsers, args=[driver3])
t4 = threading.Thread(target=browsers, args=[driver4])
t5 = threading.Thread(target=browsers, args=[driver5])

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

while True:  # prevent browser from closing when action completed
    sleep(1)
