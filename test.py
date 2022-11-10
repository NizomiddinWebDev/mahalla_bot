from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

url1 = "https://tikmate.app"

s = Service(r"C:\Users\user\Downloads\chromedriver_win32 (4)\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# try:
browser.get("https://shortsnoob.com/ru")
video = browser.find_element(by=By.XPATH, value="//*[@id='url']")
video.clear()
video.send_keys("https://youtube.com/shorts/ckJrcl_ZkFw?feature=share")
time.sleep(15)
browser.find_element(by=By.XPATH,value="//*[@id='start']").click()
ok = browser.find_element(by=By.XPATH,value="//*[@id='result']/div[1]/video/source")
result = ok.get_attribute("src")
print(result)
# except:
#         res = 0
# finally:
#     browser.quit()

# login = driver.find_element_by_css_selector("button[type='submit']").click()
#
# # save your login info?
# time.sleep(10)
# notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
# # turn on notif
# time.sleep(10)
# notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#
# # searchbox
