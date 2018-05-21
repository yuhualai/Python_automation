#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
import unittest


class Screen:
    def __init__(self, driver=None):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
                raise

        return inner


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://wwww.baidu.com")

    @Screen()
    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()

    @Screen()
    def test_02(self):
        self.driver.find_element_by_id("kw11").send_keys("yoyo")
        self.driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
