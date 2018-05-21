#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'


class Screen:
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
                raise

        return inner
