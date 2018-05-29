# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import unittest
import time
from case.lyh.ElementPage.LoginPage import LoginPage
from case.lyh.BasePage.BasePage import browser
from selenium.common.exceptions import NoSuchElementException


class login(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.login = LoginPage(self.driver)
        self.login.open("http://www.liangyihui.net/")

    def tearDown(self):
        self.driver.quit()

    def login1(self, username, psw):
        self.login.click_login()
        self.login.input_username(username)
        self.login.input_password(psw)
        self.login.click_submit()
        time.sleep(3)

    def is_login_sucess(self):
        # 判断是否获取到登录账户名称
        try:
            text = self.driver.find_element_by_class_name("header_nickname_text").text
            print(text)
            return True
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
            return False

    def test_case_01(self):
        self.login1("15921470107", "123456")
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_case_02(self):
        self.login1("15900000001", "123456")
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_case_03(self):
        self.login1("18900000001", "123456")
        result = self.is_login_sucess()
        self.assertTrue(result)
