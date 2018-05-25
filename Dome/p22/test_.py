#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from Dome.p22.Method import RunMethod
import unittest
import json


class Test_lo(unittest.TestCase):
    def setUp(self):
        self.run = RunMethod()

    def test_01(self):
        url = "http://bos.liangyihui.net/bos/event/eventlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

            "filter": {"pageIdx": 0, "pageSize": 50},
            "eventKeywords": [],
            "eventIDs": [],
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0="}

        })

        res = self.run.run_main("Post", url, data, header)
        # self.assertEqual(res['errorCode'], 1, "测试失败")

        print(res)

    def test_02(self):
        url = "http://bos.liangyihui.net/bos/event/eventlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

            "filter": {"pageIdx": 0, "pageSize": 50},
            "eventKeywords": [],
            "eventIDs": [],
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0="}

        })
        res = self.run.run_main("Post", url, data, header)
        # self.assertEqual(res['errorCode'], 0, "测试成功")

        print(res)
