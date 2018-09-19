#coding=utf-8
import time
from selenium import webdriver

#chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver"   #设置浏览器默认位置
driver = webdriver.Chrome()
driver.get("http://test.icoastline.cn/")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("V0038_01")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("submit").click()
driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[2]/div/a[2]").click()  # 点击eAudit2.0

driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/div/div[3]/div/span[3]").click() #点击常规稽核
driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]/div/span[2]").click() #点击稽核作业
driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[5]/div/div[1]").click() #稽核大类
time.sleep(1)
driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[5]/div/div[1]").click() #稽核小类
time.sleep(1)

driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[3]/div/div[7]/div/span").click()#点击线别下拉
driver.find_element_by_xpath("html/body/div[14]/div/div[2]/div/div/div[1]").click() #选择线别

driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[3]/div/div[9]/div/span").click()#点击线体下拉
driver.find_element_by_xpath("html/body/div[15]/div/div[2]/div/div/div[1]").click() #点击线体

driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[5]/div/button").click() #点击开始稽核

double1=driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[3]/div[1]") #点击稽核要求
ActionChains(driver).double_click(double1).perform()#双击稽核要求
time.sleep(1)

driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[5]/div[2]/div/button").click()#点击Pass
driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[9]/div/textarea").send_keys("autoremark")#输入稽核说明
driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[11]/div[3]/div/button").click()





#driver.quit()