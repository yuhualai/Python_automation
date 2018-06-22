#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'


import time
import unittest
from appium import webdriver
from case.lyh.BasePage.BasePage import get_desired_capabilities, get_uri
from case.lyh.ElementPage.AppPage import TestPage


class AppTest(unittest.TestCase):
    def setUp(self):
        # 获取我们设定的capabilities，通知Appium Server创建相应的会话。
        desired_caps = get_desired_capabilities()
        # 获取server的地址
        uri = get_uri()
        # 创建会话，得到driver对象，driver对象封装了所有的设备操作。
        self.driver = webdriver.Remote(uri, desired_caps)
        # 等待app完全加载
        time.sleep(3)
        self.test = TestPage(self.driver)

    def tearDown(self):
        # 测试结束，退出会话
        self.driver.quit()

    # 第1个用例"查看文章详情页面"
    def case(self):
        print(self.test.tag_text())
        self.test.tag_name()
        self.test.tag_bg()

    def test_start_01(self):
        self.case()

    def test_start_02(self):
        self.case()

    def test_start_03(self):
        self.case()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
