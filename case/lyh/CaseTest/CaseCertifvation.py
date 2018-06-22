#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from case.lyh.BasePage.LoginCookie import Cookie
from case.lyh.BasePage.BasePage import browser
import unittest
from case.lyh.ElementPage.CertificationPage import CertificationPage


class Certification(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.ck = Cookie(self.driver)
        self.ck.cookie()
        self.cert = CertificationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def article_case(self):
        self.cert.text()

    #     time.sleep(4)

    def test_article_01(self):
        self.article_case()
