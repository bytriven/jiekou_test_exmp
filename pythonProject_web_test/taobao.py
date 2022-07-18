import pytest
import datetime
import time
from selenium import webdriver

browser=webdriver.Chrome()

browser.get("https://www.taobao.com/")




if __name__ == '__main__':
    pytest.main();