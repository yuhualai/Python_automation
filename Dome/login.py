#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import requests


def login(s, url, payload):
    headers = {'Content-Type': 'application/json'}
    r = s.post(url, json=payload, headers=headers, verify=False)
    result = r.json()
    print(result)
    return result['success']


def save_box(s, url2, title, body_data):
    body = {}
    r2 = s.post(url2, data=body, verify=False)
    print(r2.url)
    return r2.url


def get_postid(u):
    import re
    postid = re.findall(r"postid=(.+?)&", u)
    print(postid)
    if len(postid) < 1:
        return ''
    else:
        return postid[0]


def delete_box(s, url3, postid):
    json3 = {"postld":postid}
    r3 = s.post(url3, json=json3, verify=False)
    print(r3.json())


if __name__ == '__main__':
    url = "http://bos.liangyihui.net/bos/event/eventlist"
    payload = {
        "filter": {"pageIdx": 0, "pageSize": 50},
        "eventKeywords": [],
        "eventIDs": [],
        "head": {"auth": "NH6tS7I2VUvZyGcJfY5xBIkB9bM/9NglXZZ6OijKDs0="}

    }
    s = requests.session()
    login(s, url, payload)