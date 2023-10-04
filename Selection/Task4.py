from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

print('start whatsapp script')
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print('Got the drivers')


search_button = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath("//input[@title='Search or start new chat']"))


search_button.click()
time.sleep(2)

search_button.send_keys("A")
time.sleep(2)


input_box = driver.find_element_by_xpath(r'//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
time.sleep(2)
input_box.send_keys("Hello" + Keys.ENTER)
time.sleep(2)
