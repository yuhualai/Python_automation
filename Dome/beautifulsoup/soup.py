#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from bs4 import BeautifulSoup

import requests

r = requests.get("http://www.cnblogs.com/yoyoketang")
blog = r.content
# print(blog)

soup = BeautifulSoup(blog, "html.parser")

times = soup.find_all(class_="dayTitle")
title = soup.find_all(class_="postTitle")
descs = soup.find_all(class_="postCon")

# for i in docidse:
#     # a = i
#     c = i.div.contents[0]
#     # print(i.a.string)
#     print(c)

for i, j, k in zip(times, title, descs):
    print(i.a.string)
    print(j.a.string)
    print(k.div.contents[0])
