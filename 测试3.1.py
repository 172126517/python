# 从selenium里面导入webdriver
from selenium import webdriver
# 由于find_element_by_* 的一系列命令已经被弃用。需使用find_element() 代替，就需要导入By包。
from selenium.webdriver.common.by import By
# 由某一个异常导致程序结束的话，可以加一个异常的捕获。
from selenium.common.exceptions import NoSuchElementException
# 导入selenium模块中的Options类
from selenium.webdriver.chrome.options import Options

import time
# 不显示浏览器，让程序在后台运行
chrome_options = Options()
chrome_options.add_argument("-headless")
chrome_options.add_argument("-disable-gpu")

# 找到插件的路径，使用它驱动操作，这里用的是默认路径"python\scripts"
driver = webdriver.Chrome(options=chrome_options)

# 选择需要打卡的网址，填入签到网页
driver.get('https://dukou.dev/')

# 设置Selenium Webdriver的隐式等待，10内。
driver.implicitly_wait(10)
# 找到邮件和密码输入框的ID,并在对应的位置送入账号密码
username = "172126517@qq.com"
Password = "Traveler1314"
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

# 对结果验证
try:
    driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/button[1]')
except NoSuchElementException:
    print("No签到Element -Exception")

# 获取流量使用情况
UseToday = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/p[1]')
UsedData = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/p[2]')
DataRemaining = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/p[3]')
print("当前套餐流量使用情况：")
print(UseToday.text)
print(UsedData.text)
print(DataRemaining.text)
# 获取签到流量使用情况
LastSign = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[3]/div[2]')
NoUsedData = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[4]/div[2]')
print("签到奖励流量：")
print("上次签到奖励", LastSign.text)
print("未转移的签到流量", NoUsedData.text)

ret = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/button[1]')
# 是不是以签到开头
print("*******************************")
if ret.text == '签 到':
    print('********* 签到成功 ************')
else:
    print('******** 今日已签到 ***********')
print("*******************************")
driver.close()


