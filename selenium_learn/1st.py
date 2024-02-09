from selenium import webdriver
import time

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(
    '/home/ilyabaykov/.config/google-chrome/Default/Extensions/khdgjhdgmblhlngkhmnmbkacgjcecnah/1.0.0_0.crx')
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(50)
