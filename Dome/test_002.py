#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HuaLai():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def quit(self):
        return self.driver.quit()


if __name__ == '__main__':
    d = HuaLai()
    d.get("https://www.lyh.com")
    input_loc = ("id", "kw")
    d.send_keys(input_loc, "yoyo")
    button_loc = ("id", "su")
    d.click(button_loc)
    d.quit()
