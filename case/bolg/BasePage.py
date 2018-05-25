#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '10.0',
        'deviceName': 'iPhone 6s',
        'appPackage': 'net.liangyihui.app',
        'appActivity': 'com.dop.h_doctor.ui.splash.IntroActivity',
        "app": "/Users/yuhualai/Desktop/oncologynews.app"

    }
    return desired_caps


def get_uri():
    return 'http://localhost:4723/wd/hub'


def get_sy():
    sys.stdout.flush()


class Action:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url, t='', timeout=10):
        # self.driver.get(url)
        # self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Erroe:%s" % msg)

    # 定位元素方法封装，参数locator是元祖类型
    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    # 定位一组元素
    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        element = self.find_element(locator)
        element.click()
        # 获取文本

    def get_text(self, locator):
        element = self.find_element(locator).text
        return element

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # 判断文本在元素里，没定位到元素返回False，定位到单号判断结果布尔值
    def is_text_in_element(self, locator, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            print(result)
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result
