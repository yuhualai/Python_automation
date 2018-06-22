# -*- coding: utf-8 -*-

' a test module '
import os

from case.lyh.BasePage import readexcel
from case.lyh.BasePage.readexcel import ExcelUtil

__author__ = 'hualai yu'

import unittest

from case.lyh.ElementPage.LoginPage import LoginPage
from case.lyh.BasePage.BasePage import browser
from selenium.common.exceptions import NoSuchElementException
import ddt
import time

#
# curpath = os.path.dirname(os.path.realpath(__file__))
# testxlsx = os.path.join(curpath, "/Users/yuhualai/PycharmProjects/yoyotest/case/lyh/BasePage/testdata.xlsx")
# testdata = readexcel.ExcelUtil(testxlsx).dict_data()

data = ExcelUtil("/Users/yuhualai/PycharmProjects/yoyotest/case/lyh/BasePage/testdata.xlsx", "Sheet1")
testdata = data.dict_data()
# print(testdata)


@ddt.ddt
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

    def is_login_sucess(self):
        # 判断是否获取到登录账户名称
        try:
            text = self.driver.find_element_by_class_name("header_nickname_text").text
            print(text)
            return True
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
            return False

    @ddt.data(*testdata)
    def test_case_01(self, data):
        self.login1(data["username"], data["password"])
        time.sleep(2)
        result = self.is_login_sucess()
        self.assertTrue(result)
