
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.taobao.com/")
driver.find_element(By.XPATH,'//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
driver.find_element(By.XPATH,'//*[@id="fm-login-id"]').send_keys('19828306892')
driver.find_element(By.XPATH,'//*[@id="fm-login-password"]').send_keys('baiyang520,.1314')
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[4]/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="J_MiniCart"]/div[1]/a/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="q"]').send_keys('美的电风扇')
times='2022-06-25 15:00:00'
while 1==1:
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    if now > times:
        while 1==1:
            try:
                if driver.find_element('结算按钮XPATH'):
                    print("here")
                    driver.find_element('结算按钮XPATH').click()
                    print(f'主人，结算成功，我帮你抢到了')

                    break
            except:
                pass







