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