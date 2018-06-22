#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import requests
import json


class RunMain:

    def send_get(self, url, data, header):
        res = requests.get(url=url, data=data, header=header).json()
        return res

    def send_post(self, url, data, header):
        res = requests.post(url=url, data=data, header=header).json()
        return res

    def run_main(self, url, method, data=None, header=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res


if __name__ == '__main__':

    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
        'cart': '11'
    }
    run = RunMain()
    # print(run.res)
# print run.run_main(url,'GET',data)
