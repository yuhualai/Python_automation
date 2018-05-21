#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Dome import LoginPage

__author__ = 'hualai yu'

' a test module '

import unittest
from selenium import webdriver


class Caselogin126mail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.url = "http://www.liangyihui.net/"
        cls.username = "15921470107"
        cls.password = "123456"

    def test_login_mail(self):
        login_page = LoginPage.LoginPage(self.driver, self.url)
        login_page.open()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
