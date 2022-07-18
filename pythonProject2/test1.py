import unittest
from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # 悬浮元素定位
from selenium.webdriver.support.select import Select  # 下拉框定位


class TestCase(unittest.TestCase):
    """ def test_01_login(self):
        # global driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("http://shop-xo.hctestedu.com/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input').send_keys("bytriven")
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys("123456")
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()"""

    def test_02_select_products(self):
        """查询商品
        ：return"""
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("http://shop-xo.hctestedu.com/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input').send_keys(
            "bytriven")
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys(
            "123456")
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
        # 进入框架的语句driver.switch_to.frame(“menu_frame框架名称")
        driver.find_element(By.LINK_TEXT, "女装").click()
        # 完成操作以后还要出框架driver.switch_to.default_content()
        # 然后进入到其他框架完成操作，这才能正确完成定位-点击的操作，driver.switch_to.frame(“main_frame框架名称")
        # sel = Select(driver.find_element(By.XPATH, '想要定位该下拉框的元素路径')) #这是定位下拉框，并且将其传入一个对象sel
        # sel.select_by_value("1/2/3/4/5")这里就是选择下拉框内的元素值，值定位是现在最常用的，另外的方法还有by_visible_text('元素名称。如手机配件‘)，还有by_index("0/1/2/3")

        # 当前网站使用的是悬浮窗口，没有框架，所以以下使用到悬浮定位,首先在在前面导入了包  import ActionChains
        ActionChains(driver).move_to_element(
            driver.find_element(By.XPATH, '//*[@id="goods-category"]/div/div/div/ul/li[1]/a/div/h3/span')).perform()
        driver.find_element(By.XPATH,'//*[@id="goods-category"]/div/div/div/ul/li[1]/div/div/div/div/div/dl[1]/dd[1]/a/span').click()
    def test_03_select_products(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("http://www.haocheng666.cn:8087/#/login")
        driver.implicitly_wait(10)
        #driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
        driver.find_element(By.XPATH, '//*[@id="login"]/div/form/div[1]/div/div[1]/input').send_keys(
            "白杨")
        driver.find_element(By.XPATH,
                            '//*[@id="login"]/div/form/div[2]/div/div/input').send_keys(
            "123456")
        driver.find_element(By.XPATH, '//*[@id="login"]/div/form/div[3]/div/button').click()
