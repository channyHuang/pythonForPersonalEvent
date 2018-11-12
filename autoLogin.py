import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://login.51job.com/login.php?lang=c&url=http%3A%2F%2Fwww.51job.com%2Fguangzhou%2F')
browser.find_element_by_id("loginname").send_keys("349117102@qq.com")
browser.find_element_by_id("password").send_keys("c3d4i9A1A1**")
#browser.find_element_by_id("login_btn").click()
browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)
browser.find_element_by_id("login_btn").send_keys(Keys.RETURN)

time.sleep(20)

print("next page")
browser.switch_to_window(browser.window_handles[0])
browser.find_element_by_partial_link_text(u"倩").click()



