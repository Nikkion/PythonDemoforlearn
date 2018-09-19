# -*- coding: utf-8 -*-
import HTMLTestRunnerScreenshot
import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver import ActionChains


class EAuditZC_record(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.icoastline.cn:5566"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_e_audit20_zc(self):
        # Step稽核人登录-开始稽核
        driver = self.driver
        driver.get(self.base_url + "/logon.html")
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time()))
        # current_time1 = time.strftime("%Y-%m-%d", time.localtime(time()))
        # print current_time
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("V0038_01")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[2]/div/a[2]").click()  # 点击eAudit2.0

        driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div[4]/div").click()  # 点击现场稽核

        time.sleep(2)

        # fixme
        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[7]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[12]/div/div[2]/div/div/div").click()#品牌


        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[9]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[13]/div/div[2]/div/div/div").click()#ODM

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[11]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[14]/div/div[2]/div/div/div").click()#客户

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[13]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[15]/div/div[2]/div/div/div").click()#系列

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[15]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div").click()#机种

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[17]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[17]/div/div[2]/div/div/div").click()#物料名称

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[19]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[18]/div/div[2]/div/div/div").click()#物料编号
        time.sleep(1)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[22]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[19]/div/div[2]/div/div/div[1]").click()#制程

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[24]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[20]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]").click()#线体

        time.sleep(2)



        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/button").click()  # 点击确定开始稽核
        time.sleep(1)


        double=driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div")
        ActionChains(driver).double_click(double).perform()
        time.sleep(1)
        select=driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[11]/select/option[2]")
        select.click()
        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div").click()
        time.sleep(1)

        # driver.find_element_by_xpath(
        #     "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div").click()



        # aa = driver.find_element_by_xpath("html/body/div[24]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
        # aa.click()
        # ActionChains(driver).double_click(aa).perform()
        # bb = driver.find_element_by_xpath("html/body/div[24]/div/div[2]/div/div[2]/div[2]/div/div[4]/input")
        # time.sleep(1)
        # bb.send_keys("22")
        #
        # time.sleep(1)
        # driver.find_element_by_xpath("html/body/div[24]/div/div[1]/div/div/div[5]").click()
        #
        # time.sleep(1)
        #
        # cc = driver.find_element_by_xpath(
        #     "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div[3]/div")
        # cc.click()
        # # ActionChains(driver).double_click(cc).perform()
        #
        # time.sleep(2)
        # select = driver.find_element_by_xpath(
        #     "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[11]/select/option[2]")
        # select.click()
        #
        # time.sleep(1)
        # remark = driver.find_element_by_xpath(
        #     "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[9]/div[3]/div")
        # remark.click()
        # remark_input = driver.find_element_by_xpath(
        #     "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[11]/input")
        # remark_input.send_keys("1120")
        # time.sleep(1).e

        other = driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div")
        ActionChains(driver).double_click(other).perform()

        time.sleep(1)


        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/button").click()#点击确定

        driver.find_element_by_xpath("html/body/div[25]/div[2]/div[1]/div").click()#点击确定提示

        driver.save_screenshot("D:\\xujun\\report\\"+now+"Ngrecord.png")

        #Step稽核人查看记录并对任务截图保留
        time.sleep(2)
        driver.find_element_by_xpath(
            "html/body/div[3]/div[1]/div/div[2]/div/a[2]").click()#点击eAudit2.0

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div[5]/div/span[2]").click() #点击稽核记录
        time.sleep(2)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[4]/div/button").click() #点击查询
        time.sleep(2)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[3]/div/div[2]/div/div[3]/div[3]/div/div/div[2]/div[3]/div/div[6]/div[1]/a[1]").click()#点击第一条记录查看
        time.sleep(2)
        js = "a = document.getElementsByClassName('webix_ss_center')[1];" \
             "b = document.getElementsByClassName('webix_hs_center')[2];" \
             "a.scrollTo(10000,0);" \
             "b.scrollTo(10000,0);"
        driver.execute_script(js) #JS拖动横向滚动条
        driver.save_screenshot("D:\\xujun\\report\\"+now+"state.png")#保存图像
        time.sleep(2)

        js1 ="a = document.getElementsByClassName('webix_icon_button')[4];"\
            "a.click();"
        driver.execute_script(js1)#js关闭任务按钮

        time.sleep(2)

        #Step处理人开始处理稽核任务
        driver.find_element_by_xpath(
            "html/body/div[3]/div[1]/div/div[2]/div/a[1]").click()#点击主页
        time.sleep(1)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]").click()#点击eAudit2.0任务
        time.sleep(1)
        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]").click()#点击制程稽核任务
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[3]/div/div[2]/div[1]/span").click()

        time.sleep(1)

        js2 ="document.getElementsByClassName('webix_view webix_scrollview eaudit_task_form')[0].scrollTo(0,200);"
        driver.execute_script(js2)

        time.sleep(2)
        #fixme
        double1=driver.find_element_by_xpath(
            "html/body/div[12]/div/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div[1]/div/textarea")
        ActionChains(driver).double_click(double1).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "html/body/div[12]/div/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div[1]/div/textarea").send_keys("autoremark")
        time.sleep(1)
        driver.save_screenshot("D:\\xujun\\report\\taskplay.png")
        driver.find_element_by_xpath(
            "html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/button").click()#点击确定


        #fixme
        #step审批人登录
        driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[3]/div/div/div/span[1]").click()#点击用户名
        driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div/div/a[2]").click()#点击注销
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("V0038_02")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        time.sleep(1)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[1]/div/div[2]/div/a[1]").click()  # 点击主页
        time.sleep(1)

        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]").click()  # 点击eAudit2.0任务
        time.sleep(1)
        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]").click()  # 点击制程稽核任务
        driver.find_element_by_xpath(
            "html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[3]/div/div[2]/div[1]/span").click()# 点击制程稽核任务
        driver.save_screenshot("D:\\xujun\\report\\"+now+"re-taskplay.png")


        js3 = "document.getElementsByClassName('webix_view webix_scrollview eaudit_task_form')[0].scrollTo(0,600);"
        driver.execute_script(js3)

        time.sleep(2)

        double1 = driver.find_element_by_xpath(
            "html/body/div[10]/div/div[2]/div/div[1]/div/div/div/div[4]/div[2]/div/textarea")
        ActionChains(driver).double_click(double1).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "html/body/div[10]/div/div[2]/div/div[1]/div/div/div/div[4]/div[2]/div/textarea").send_keys(
            "autoapprove")
        time.sleep(1)
        driver.save_screenshot("D:\\xujun\\report\\"+now+"re-taskplay1.png")
        driver.find_element_by_xpath(
            "html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/button").click()

    def test_e_audit20_cg(self):
        
        driver = self.driver
        driver.get(self.base_url + "/logon.html")
        
        #时间信息设置
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))


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

        double1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[2]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[3]/div[1]/div") #点击稽核要求
        ActionChains(driver).double_click(double1).perform()#双击稽核要求
        time.sleep(1)

        driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[5]/div[2]/div/button").click()#点击Pass
        driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[9]/div/textarea").send_keys("autoremark")#输入稽核说明
        driver.find_element_by_xpath("html/body/div[16]/div/div[2]/div/div/div[11]/div[3]/div/button").click()




        


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    # 添加测试用例到测试套件中
    # testunit.addTest(EAuditZC_record("test_e_audit20_zc"))
    testunit.addTest(EAuditZC_record("test_e_audit20_cg"))
    # testunit.addTest(EAuditCG("test_e_audit20_cg"))
    # testunit.addTest(EAuditCG("test_e_audit20_cg"))
    # 定义个报告存放路径
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:\\xujun\\report\\' + now + 'result.html'
    fp = file(filename, 'wb')

    runner =HTMLTestRunnerScreenshot.HTMLTestRunner(
        stream=fp,
        title=u'制程稽核测试报告',
        description=u'用例执行情况：',
         )
    # 运行测试用例
    runner.run(testunit)
    # 关闭报告文件
    fp.close()