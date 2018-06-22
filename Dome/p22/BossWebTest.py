#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import json

import unittest

from Dome.p22.Method import RunMethod


class Test(unittest.TestCase):
    def setUp(self):
        self.run = RunMethod()
        self.header = {'Content-Type': 'application/json'}

    def test_event_01(self):
        url = "http://bos.liangyihui.net/bos/event/eventlist"
        data = json.dumps({

            "filter": {"pageIdx": 0, "pageSize": 50},
            "eventKeywords": [],
            "eventIDs": [],
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0="},
            # 'errorCode': 1001,

        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, self.header)
        print(res)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

        # self.assertEqual(res["errorCode"], 0, "测试成功")

    def test_event_02(self):
        url = "http://bos.liangyihui.net/bos/event/eventlist"
        data = json.dumps({

            "filter": {"pageIdx": 0, "pageSize": 50},
            "eventKeywords": [],
            "eventIDs": [],
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0="}

        })
        res = self.run.run_main("Post", url, data, self.header)
        # print(res)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_columnist_01(self):
        url = "http://bos.liangyihui.net/bos/columnist/getcolumnistlist"
        data = json.dumps({
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0=", "cid": "TestData_CID"},
            "filter": {"pageIdx": 0, "pageSize": 500}
        })
        res = self.run.run_main("Post", url, data, self.header)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_columnist_02(self):
        url = "http://bos.liangyihui.net/bos/columnist/getcolumnistlist"
        data = json.dumps({
            "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0=", "cid": "TestData_CID"},
            "filter": {"pageIdx": 0, "pageSize": 500}
        })

        res = self.run.run_main("Post", url, data, self.header)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")
