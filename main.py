import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://10fastfingers.com/typing-test/indonesian")
textField = driver.find_element_by_id("inputfield")
textField.clear()
time.sleep(6)
while True:
    word = driver.find_element_by_xpath('.//span[@class = "highlight"]')
    print(word.text)
    textField.send_keys(word.text)
    textField.send_keys(Keys.SPACE)
    time.sleep(0.2)
