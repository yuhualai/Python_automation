#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from Dome.p22.Method import RunMethod
import unittest
import json
import urllib3


class Test(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings()
        self.run = RunMethod()

    def test_get_document_01(self):
        url = "https://www.liangyihui.net/api/doc/getdocumentlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({
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
                "auth": "xBEYbAd7vMEcCr+KOLZUlxEo9M6r4Oi8r8kFhoLvdmI=",
                "auth2": "SZrqOrFibfRkKPRIm7bzvA=="
            },
            "filters": [{
                "items": [{
                    "filterId": 8,
                    "type": 1
                }],
                "filterGroupId": 18
            }],
            "sort": {
                "pageIdx": 0,
                "pageSize": 10,
                "startTime": 0
            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        # print(res)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_get_document_02(self):
        url = "https://www.liangyihui.net/api/doc/getdocumentlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({
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
                "auth": "xBEYbAd7vMEcCr+KOLZUlxEo9M6r4Oi8r8kFhoLvdmI=",
                "auth2": "SZrqOrFibfRkKPRIm7bzvA=="
            },
            "filters": [{
                "items": [{
                    "filterId": 8,
                    "type": 1
                }],
                "filterGroupId": 18
            }],
            "sort": {
                "pageIdx": 0,
                "pageSize": 10,
                "startTime": 0
            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_get_recommended_01(self):
        url = "https://www.liangyihui.net/api/doc/getdocumentlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

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
                "auth": "jL+GhwhD6B\/8fyysYNQi49LQCpWpYfHjyd\/H125UNxY=",
                "auth2": "hePPo8hp0kk2e1\/Q+qYCrw=="
            },
            "filters": [{
                "items": [{
                    "filterId": 1
                }],
                "filterGroupId": 1
            }],
            "sort": {
                "pageIdx": 0,
                "pageSize": 40,
                "startTime": 0

            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        # print(res["docGroups"][0]["documents"][0]["title"])
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_get_recommended_02(self):
        url = "https://www.liangyihui.net/api/doc/getdocumentlist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

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
                "auth": "jL+GhwhD6B\/8fyysYNQi49LQCpWpYfHjyd\/H125UNxY=",
                "auth2": "hePPo8hp0kk2e1\/Q+qYCrw=="
            },
            "filters": [{
                "items": [{
                    "filterId": 1
                }],
                "filterGroupId": 1
            }],
            "sort": {
                "pageIdx": 0,
                "pageSize": 40,
                "startTime": 0

            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        # print(res["docGroups"][0]["documents"][1]["title"])
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_get_func_block_01(self):
        url = "https://www.liangyihui.net/api/doc/getfuncblocklist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

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

                "auth": "jL+GhwhD6B\/8fyysYNQi49LQCpWpYfHjyd\/H125UNxY=",
                "auth2": "hePPo8hp0kk2e1\/Q+qYCrw=="
            },
            "sort": {
                "pageIdx": 0,
                "pageSize": 5,
                "startTime": 1528946677.599436
            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        # print(res["blockGroups"][1]['documents'][0]['picUrl'])
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")

    def test_get_func_block_02(self):
        url = "https://www.liangyihui.net/api/doc/getfuncblocklist"
        header = {'Content-Type': 'application/json'}
        data = json.dumps({

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

                "auth": "jL+GhwhD6B\/8fyysYNQi49LQCpWpYfHjyd\/H125UNxY=",
                "auth2": "hePPo8hp0kk2e1\/Q+qYCrw=="
            },
            "sort": {
                "pageIdx": 0,
                "pageSize": 5,
                "startTime": 1528946677.599436
            }
        })
        # res = mock_test(self.run.run_main, "Post", url, data, header, data)

        res = self.run.run_main("Post", url, data, header)
        # print(res["blockGroups"][1]['documents'][1]["title"])
        self.assertEqual(res['responseStatus']['errorcode'], 0, "测试成功")
