#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
import unittest

import ddt
import time

import os
from selenium.webdriver.android import webdriver

from Dome.ddt import readexcel


__author__ = 'hualai yu'


curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "demo_api.xlsx")
testdata = readexcel.ExcelUtil(testxlsx).dict_data()
print(testdata)


@ddt.ddt
class Bolg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self, username, psw):
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_sucess(self):
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    @ddt.data(*testdata)
    def test_login(self, data):
        print("当前测试数据%s" % data)
        self.login(data["username"], data["password"])
        result = self.is_login_sucess()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
