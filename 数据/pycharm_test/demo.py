# from selenium import webdriver

# driver = webdriver.Chrome()# 打开Chrome浏览器
# driver.get('https://www.baidu.com/')
# driver.find_element("id", 'kw').send_keys('中华诗歌网')
# driver.find_element('id', 'su').click()
# driver.close()# 关闭当前页面, 浏览器只打开了一个页签时,与driver.quit()效果一致
# driver.quit()# 关闭driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestCase(unittest.TestCase):

    def test_01_login(self):
        # global driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = option)
        driver.get("http://www.haocheng666.cn:8087/#/login/")
        driver.find_element(By.XPATH, "//*[@id='login']/div/form/div[1]/div/div[1]/input").send_keys("白杨")
        driver.find_element(By.XPATH, "//*[@id='login']/div/form/div[2]/div/div/input").send_keys("123456")
        driver.find_element(By.XPATH, "//span[text()='登录']").click()