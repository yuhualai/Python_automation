#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from bs4 import BeautifulSoup

import requests
import os

r = requests.get("http://sc.chinaz.com/tupian/beijingtupian.html")
blog = r.content

soup = BeautifulSoup(blog, "html.parser")
image = soup.find_all(class_="box")

for i in image:
    jpg_rl = i.div.a["href"]
    title = i.div.a.img["alt"]
    print(title)
    print(jpg_rl)
    print("")
    with open(os.getcwd() + "\\jpg\\" + title + '.htm', "wb") as f:
        f.write(requests.get(jpg_rl).content)

