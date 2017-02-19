from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

time.sleep(5)
browser.quit()
