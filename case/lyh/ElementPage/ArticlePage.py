#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from case.lyh.BasePage.BasePage import Action


class ArticlePage(Action):
    ls_name = ("css selector", ".block_unit_news>.block_unit>.block_unit_right>.block_unit_title")
    ls_do = ("css selector", ".dotdotdot")
    ls_a = ("css selector", ".sidebar_hot_unit_right a")
    article = ("css selector", ".h1-title")
    project = ("css selector", ".column_title")
    # project = ("css selector", ".column_title")

    def list_text(self):
        ls = self.find_elements(self.ls_name)
        return ls

    def list_do(self):
        ls = self.find_elements(self.ls_do)
        return ls

    def list_a(self):
        ls = self.find_elements(self.ls_a)
        return ls

    def list_article(self):
        ls = self.get_text(self.article)
        return ls

    def list_project(self):
        ls = self.get_text(self.project)
        return ls
