#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'


import requests
import urllib3
urllib3.disable_warnings()
import json


# 先打开登录首页，获取部分cookie
s = requests.session()
url = "https://passport.cnblogs.com/user/signin"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
payload = {"input1":"yuhualai", "input2":"yu.87579272", "remember":True}


r = s.post(url, json=payload, headers= headers, verify=False)
# print(r.json())
print(r.json())

# data2={'user_login':'test1','email':'1234567@163.com','createuser':'添加用户'}

# url2 = "http://www.liangyihui.net/account/collection/article"
# r2=s.post(url2)
# print(r2.text)

# c = requests.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', 's%3Aocs5JnG9dqJS9jUuhHn_5JKoG2flld6C.jwm%2BgdL5rDfzb3yGhOPvA2oG7YEErL%2FFGp%2FDnTmFTKY')
# # c.set('.Cnblogs.AspNetCore.Cookies','passport.cnblogs.com')# 填上面抓包内容
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print(s.cookies)


# r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
# url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR":"FE27D343",
#         "Editor$Edit$txbTitle":"这是博客主题：上海-悠悠",
#         "Editor$Edit$EditorBody":"<p>这里正文内容：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished":"on",
#         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#         "Editor$Edit$Advanced$chkComments":"on",
#         "Editor$Edit$Advanced$chkMainSyndication":"on",
#         "Editor$Edit$Advanced$txbEntryName":"",
#         "Editor$Edit$Advanced$txbExcerpt":"",
#         "Editor$Edit$Advanced$tbEnryPassword":"",
#         "Editor$Edit$lkbDraft":"存为草稿",
#         }
# r2 = s.post(url2, data=body, verify=False)
# print(r.content)