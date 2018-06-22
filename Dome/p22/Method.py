#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'hualai yu'

import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        # return json.dumps(res, ensure_ascii=False)
        return res
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
#