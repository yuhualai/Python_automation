#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")


def find_element(locator, timeout=10):
    # 等待时长10秒，默认0.5秒询问一次
    element = WebDriverWait(driver, timeout).until(lambda x: x.find_element(*locator))
    return element


# 封装后代码
input_loc = ("id", "kw")
button_loc = ("id", "su")
find_element(input_loc).send_keys("yoyo")
find_element(button_loc).click()

# 判断id为kw元素是否消失
is_disappeared = WebDriverWait(driver, 10, 1).until_not(lambda x: x.find_element("id", "kww").is_displayed())
print(is_disappeared)

driver.quit()
