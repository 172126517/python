from selenium import webdriver

import time

# 找到插件的路径，使用它驱动操作
driver = webdriver.Chrome()

# 选择需要打卡的网址，填入签到网页
driver.get('https://dukou.dev/')

# 找到邮件和密码输入框的ID,并在对应的位置送入账号密码
username = "172126517@qq.com"
Password = "Traveler1314"
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('passwd').send_keys(Password)

# 找到登录按钮的xpath，模拟点击
driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()

#设置Selenium Webdriver的隐式等待，10内。
driver.implicitly_wait(10)
# 找到签到按钮的xpath，模拟签到
driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/button[1]').click()

#等待2秒后，关闭窗口
time.sleep(2)
driver.close()





