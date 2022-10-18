# 从selenium里面导入webdriver
from selenium import webdriver
# 由于find_element_by_* 的一系列命令已经被弃用。需使用find_element() 代替，就需要导入By包。
from selenium.webdriver.common.by import By
# 由某一个异常导致程序结束的话，可以加一个异常的捕获。
from selenium.common.exceptions import NoSuchElementException

import time

# 找到插件的路径，使用它驱动操作，这里用的是默认路径"python\scripts"
driver = webdriver.Chrome()

# 选择需要打卡的网址，填入签到网页
driver.get('https://dukou.dev/')

# 找到邮件和密码输入框的ID,并在对应的位置送入账号密码
username = "17*****@qq.com"
Password = "Tr******"
try:
    driver.find_element(By.ID, "email").send_keys(username)
except NoSuchElementException:
    print("NoEmailElement -Exception")
try:
    driver.find_element(By.ID, "passwd").send_keys(Password)
except NoSuchElementException:
    print("NoPasswdElement -Exception")

# 找到登录按钮的xpath，模拟点击
driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[3]/div/div/span/button').click()

# 设置Selenium Webdriver的隐式等待，10内。
driver.implicitly_wait(10)
# 找到签到按钮的xpath，模拟签到
driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/button[1]').click()

# 等待2秒后，关闭窗口
time.sleep(2)


driver.close()

