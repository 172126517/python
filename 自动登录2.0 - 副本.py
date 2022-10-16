from selenium import webdriver
import time

# 找到插件的路径，使用它驱动操作
driver = webdriver.Chrome()

# 填入签到网页
driver.get('https://dukou.dev/')

# 在username和Password后面输入账号密码
username = "1721***@qq.com"
Password = "1234****"
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('passwd').send_keys(Password)

# 登录
driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()

#设置Selenium Webdriver的隐式等待，10内。
driver.implicitly_wait(10)

# 签到
driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/button[1]').click()

#等待2秒后，自动关闭窗口
time.sleep(2)
driver.close()





