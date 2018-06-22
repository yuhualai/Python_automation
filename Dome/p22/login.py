#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import requests


class Blog():
    def __init__(self, s):
        self.s = s

    def login(self):
        url = "https://www.liangyihui.net/api/user/getuserinfo"
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
        res = self.s.post(url, headers=header, json=data, verify=False).json()
        return res


if __name__ == '__main__':
    s = requests.session()
    Blog(s).login()
