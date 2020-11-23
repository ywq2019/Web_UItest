# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

executable_path = r"D:\PythonProject\Web_UItest\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver)

driver = WebChrome(executable_path)

driver.implicitly_wait(20)
driver.get("http://www.hqwx.com/")
driver.maximize_window()
driver.switch_to_alert().accept()
driver.find_element_by_id('kw').send_keys('Airtest')