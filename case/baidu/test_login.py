#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import unittest

from case.baidu.LoginPage import LoginPage
from case.baidu.BasePage import browser
from case.baidu.screen import Screen


class Login_test(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.login = LoginPage(self.driver)
        self.login.open("http://www.liangyihui.net/")

    def tearDown(self):
        self.driver.quit()

    def login_case(self, username, psw, expect=True):
        # 点击登录按钮，弹出登录框
        self.login.click_login()
        # 操作用户名
        self.login.input_username(username)
        # 操作密码
        self.login.input_password(psw)
        # 点击登录提交按钮
        self.login.click_submit()
        # 判断昵称获取是否正确
        result = self.login.is_text_in_element(("class name", "header_nickname_text"), "刚刚")
        expect_result = expect
        self.assertEquals(result, expect_result)

    # @Screen(driver)
    def test_login_01(self):
        # 输入用户名和密码
        self.login_case("15921470107", "123456", True)

    # @Screen(driver)
    def test_login_02(self):
        # 输入用户名和密码
        self.login_case("15900000012", "123456", False)

    # @Screen(driver)
    def test_login_03(self):
        # 输入用户名和密码
        self.login_case("18900000001", "123456", False)
