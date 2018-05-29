#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import unittest
from case.lyh.BasePage.BasePage import browser
from case.lyh.ElementPage.SearchPage import SearchPage
from selenium.common.exceptions import NoSuchElementException


class Search(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.Search = SearchPage(self.driver)
        self.Search.open("http://www.liangyihui.net/")

    def tearDown(self):
        self.driver.quit()

    def Search_case(self, text):
        self.Search.input_Box(text)
        self.Search.input_Btn()

        self.Search.window_handles(1)
        try:
            print(self.Search.input_text(1))
            return True
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
            return False

    def test_search_01(self):
        self.Search_case("癌症")

    def test_search_02(self):
        self.Search_case("哈哈")

    def test_search_03(self):
        self.Search_case("乳腺癌")
