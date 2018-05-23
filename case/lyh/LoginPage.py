#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

from case.lyh.BasePage import Action


class LoginPage(Action):
    # 定位页面元素，定位器
    login = ("id", "login")
    login1_mobile = ("id", "login1_mobile")
    password = ("name", "password")
    classmate = ("class name", "btn")
    name_txt = ("class name", "header_nickname_text")

    # 获取登录元素
    def click_login(self):
        self.click(self.login)

    # 输入账号框
    def input_username(self, username):
        self.send_keys(self.login1_mobile, username)

    # 输入密码框
    def input_password(self, password):
        self.send_keys(self.password, password)

    # 登录按钮
    def click_submit(self):
        self.click(self.classmate)

    def text_name(self):
        self.txt(self.name_txt)
