#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

from case.baidu.BasePage import Action


class LoginPage(Action):
    login = ("id", "login")
    login1_mobile = ("id", "login1_mobile")
    password = ("name", "password")
    classmate = ("class name", "btn")
    name_txt = ("class name", "header_nickname_text")

    def input_username(self, username):
        self.send_keys(self.login1_mobile, username)

    def input_password(self, password):
        self.send_keys(self.password, password)

    def click_submit(self):
        self.click(self.classmate)

    def click_submit1(self):
        self.click(self.login)

    def text_name(self):
        self.txt(self.name_txt)
