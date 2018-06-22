#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
import ddt
import unittest

__author__ = 'hualai yu'

testData = [{"uesername": "selenium群", "psw": "24298934"},
            {"uesername": "java群", "psw": "24298934"},
            {"uesername": "python群", "psw": "24298934"},
            {"uesername": "appium群", "psw": "24298934"},
            ]


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    @ddt.data(*testData)
    def test_ddt(self, data):
        print(data)


if __name__ == '__main__':
    unittest.main()
