from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

async def instagramVideo(url):
    s = Service(r"C:\Users\user\Downloads\chromedriver_win32_one\chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    if "www.instagram.com/p/" in url:
        url = url.replace("www.instagram.com", "imginn.com")
    else:
        url = re.sub(r"www.instagram.com/\b[a-z]\w/", "imginn.com/p/", url)
    print(url)
    browser.get(url)
    video = browser.find_element(by=By.CLASS_NAME, value="video-wrap")
    return video.get_attribute('data-video')

# url = 'https://imginn.com/p/CYTTiOiJ1If/'
# "https://www.instagram.com/p/CYTTiOiJ1If/"

