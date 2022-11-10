from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re


async def shortYt(url):
    s = Service(r"C:\Users\user\Downloads\chromedriver_win32 (4)\chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    try:
        browser.get("https://shortsnoob.com/ru")
        video = browser.find_element(by=By.XPATH, value="//*[@id='url']")
        video.clear()
        video.send_keys(url)
        await sleep(10)
        browser.find_element(by=By.XPATH, value="//*[@id='start']").click()
        ok = browser.find_element(by=By.XPATH, value="//*[@id='result']/div[1]/video/source")
        result = ok.get_attribute("src")
    except:
        result = 0
    finally:
        browser.quit()
    return result
