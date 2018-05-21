#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def browser(browser='firefox'):
    try:
        if browser == 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can enter 'firefox', 'chrome', 'ie', or 'phantomjs'")
    except Exception as msg:
        print("%s" % msg)


class HuaLai:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url, t='', timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()

        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Erroe:%s" % msg)

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            print(result)
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result


if __name__ == '__main__':
    driver = browser()
    driver1 = browser("chrome")