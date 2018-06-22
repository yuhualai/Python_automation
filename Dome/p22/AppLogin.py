#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
import json

from Dome.p22.Method import RunMethod

__author__ = 'hualai yu'

import unittest
import urllib3
import requests
from Dome.p22.login import Blog


class Test(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings()
        s = requests.session()
        self.blog = Blog(s)
        self.run = RunMethod()

    def test_login(self):
        re = self.blog.login()
        self.assertEqual(re["basic"]["name"], "张医生", "测试成功")

    def test_get_document_02(self):
        url = "https://www.liangyihui.net/api/mymessage/mymessagestatusafter47"
        header = {'Content-Type': 'application/json'}
        data = {
            "head": {
                "cid": "DCF8C8D4-3CF6-4AE7-8BE1-87E9BAF160D8",
                "cver": "4.12.1",
                "sid": "Model:iPhone---Version:10.3.3",
                "extensions": [{
                    "name": "platform",
                    "value": "iOS"
                }, {
                    "name": "phone_type",
                    "value": "iPhone 6"
                }, {
                    "name": "phene_vesion",
                    "value": "10.3"
                }],
                "auth": "GYnp211s3nfT4RYcKfAAXBKkpUF1hRUEYTskiYSY3ig=",
                "auth2": "1\/I\/GagBq+oSVhQeWhwuFg=="
            }
        }
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        print(res)
        # self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")
