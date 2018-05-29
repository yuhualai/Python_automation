#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from case.lyh.BasePage.BasePage import Action


class SearchPage(Action):
    inBox = ("id", "inputBox")
    inBtn = ("id", "formBtn")
    intxts = ("css selector", ".block_unit_title")

    def input_Box(self, text):
        self.send_keys(self.inBox, text)

    def input_Btn(self):
        self.click(self.inBtn)

    def input_text(self, i):
        io = self.texts(self.intxts, i)
        return io
