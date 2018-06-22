#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("http://www.liangyihui.net/")
c1 = {'name': 'session', 'value': 's%3AqqtmVxfBAR9AOxluZvrUPQW7b-MHLnQu.sghlwsLAMOoaxH%2F624XKkdthe4Y0H%2Bqs59olvaQRSqo'}
c2 = {'name': 'Hm_lvt_0543c91a350042875a2359a01796641a', 'value': '1528265050'}
c3 = {'name': 'Hm_lpvt_0543c91a350042875a2359a01796641a', 'value': '1528265055'}
# print(driver.get_cookies())

driver.add_cookie(c1)
# driver.add_cookie(c2)
# driver.add_cookie(c3)
time.sleep(3)

driver.refresh()


#
# driver.get("http://www.liangyihui.net/")
# driver.find_element_by_id("login").click()
# driver.find_element_by_id("login1_mobile").send_keys("15900000002")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_class_name("btn").click()
# print(driver.get_cookies())
