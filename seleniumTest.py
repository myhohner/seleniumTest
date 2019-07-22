import time

from selenium import webdriver

browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get("http://www.baidu.com")
id = browser.find_element_by_xpath('//input[@id="kw"]')
button = browser.find_element_by_id('su')

id.send_keys('slenium+python')
time.sleep(2)
id.clear()
id.send_keys('slenium+java')
time.sleep(2)
button.click()
time.sleep(2)
browser.quit()
