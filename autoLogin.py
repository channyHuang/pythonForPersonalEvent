#coding: utf-8
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image

userName = "userName"
password = "password"

def refresh51():
	browser = webdriver.Firefox()
	browser.get('https://login.51job.com/login.php?lang=c&url=http%3A%2F%2Fwww.51job.com%2Fguangzhou%2F')
	browser.find_element_by_id("loginname").send_keys(userName)
	browser.find_element_by_id("password").send_keys(password)
	#browser.find_element_by_id("login_btn").click()
	browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)
	browser.find_element_by_id("login_btn").send_keys(Keys.RETURN)
	time.sleep(5)
        browser.find_element_by_xpath("//*[text()='我的51Job']").click()
	browser.find_element_by_xpath("//*[text()='刷新']").click()

	time.sleep(5)

	browser.close()

def loginZhihu():
    browser = webdriver.Firefox()
    browser.get('https://www.zhihu.com/signup?next=%2F')
    time.sleep(3)
    signBtn = browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[2]/span")
    if signBtn.text == '登录'.decode('utf-8'):
        signBtn.click()
    time.sleep(2)
    #browser.find_element_by_id('username')
    #browser.find_element_by_id('password')
    browser.find_element_by_class_name("Login-socialLogin").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@class='Login-socialButtonGroup']/button[2]").click()
    time.sleep(2)
    browser.find_element_by_id("userId").send_keys(userName)
    browser.find_element_by_id("passwd").send_keys(password)
    #browser.find_element_by_xpath("//*[@name='authZForm']/div/div[2]/div/p/a").send_keys(Keys.ENTER)
    submitBtn = browser.find_element_by_xpath("//*[@class='oauth_formbtn']/a[1]") 
    submitBtn.click()
    submitBtn.click()
    submitBtn.click() 
     
    time.sleep(5) 
    
    browser.find_element_by_id("email").click()
    submitBtn = browser.find_element_by_xpath("//*[@class='oauth_formbtn']/a[1]") 
   
    submitBtn.click()
    time.sleep(2)

def refreshLiepin():
    browser = webdriver.Firefox()   
    browser.get("https://www.liepin.com/user/login/?url=http%3A%2F%2Fc.liepin.com%2F%3Ftime%3D1541116365554")
    browser.find_element_by_xpath("//*[text()='马上登录']").click()
    browser.find_element_by_name("user_login").send_keys(userName)
    browser.find_element_by_xpath("//*[@class='login-form']/div[2]/input").send_keys(password)
    browser.find_element_by_xpath("//*[@class='login-form']/div[3]/input").submit()
    time.sleep(5)
    browser.find_element_by_xpath("//*[@class='clearfix']/li/a").click()
    time.sleep(3)
    browser.close()

def refreshZhuopin():
    browser = webdriver.Firefox()
    browser.get("https://www.highpin.cn/")
    browser.find_element_by_id("seekerUserName").send_keys(userName)
    browser.find_element_by_id("seekerPassword").send_keys(password)
    '''
    imgElement = browser.find_element_by_id("identifying_code")
    imgSize = imgElement.size
    imgLocation = imgElement.location
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    browser.save_screenshot("code.png")
    login = Image.open("code.png")  
    frame4=login.crop(rangle)  
    frame4.save('code.png')
    authcodeImg = Image.open('code.png')
    verCode = pytesseract.image_to_string(authcodeImg).strip()
    print(verCode) 
    '''
    verCode = raw_input("Input ver code:")
  
    browser.find_element_by_id("seekerVerCode").send_keys(verCode)
    browser.find_element_by_id("personSubmitBtn").click()
    time.sleep(5)
    browser.find_element_by_class_name("icon_refresh").click()
    time.sleep(5)
    browser.close()

def loginBoss():
    browser = webdriver.Firefox()
    browser.get("https://www.zhipin.com/?ka=header-home")
    browser.find_element_by_xpath("//*[text()='登录']").click()
    time.sleep(3)
    browser.find_element_by_class_name("link-scan").click()
    time.sleep(3)

if __name__ == '__main__':
    web = raw_input("input web: (51, zhihu, liepin, zhuopin, boss):")
    if (web == '51'):
        refresh51()
    elif (web == 'zhihu'):
        loginZhihu()
    elif (web == 'liepin'):
        refreshLiepin()
    elif (web == 'boss'):
        loginBoss()
    elif (web == 'zhuopin'):
        refreshZhuopin()
    else:
        refresh51()
        refreshLiepin()
        refreshZhuopin()
        loginBoss()
  
