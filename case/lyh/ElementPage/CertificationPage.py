#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
from selenium.webdriver import ActionChains

from case.lyh.BasePage.BasePage import Action


class CertificationPage(Action):
    # 定位页面元素，定位器

    name_txt = ("class name", "header_nickname_text")

    def text(self):
        mouse = self.find_element(self.name_txt)
        ActionChains(self.driver).move_to_element(mouse).perform()
