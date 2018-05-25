#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from case.bolg.BasePage import Action


class TestPage(Action):
    name = ("name", "随便看看>>")
    bq = ("name", "企业人士")

    def tag_name(self):
        self.click(self.name)

    def tag_text(self):
        name = self.get_text(self.name)
        return name

    def tag_bg(self):
        self.click(self.bq)