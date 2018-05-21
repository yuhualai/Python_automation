# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

import unittest
import time


class BlogHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        url = "http://www.liangyihui.net/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self, username, psw):
        self.driver.find_element_by_id("login").click()
        self.driver.find_element_by_id("login1_mobile").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_class_name("btn").click()
        time.sleep(3)

    def is_login_sucess(self):
        try:
            text = self.driver.find_element_by_class_name("header_nickname_text").text
            print(text)
            return True
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
            return False

    def test_01(self):
        self.login("15921470107", "123456")
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_02(self):
        result = self.is_login_sucess()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
