#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from case.baidu.BasePage import browser
from case.baidu.ArticlePage import ArticlePage
import unittest


class Article_test(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.Article = ArticlePage(self.driver)
        self.Article.open("http://www.liangyihui.net/")

    def tearDown(self):
        self.driver.quit()

    def article_case(self, lis):
        for lists in lis:
            print(lists.text)
            # 获取当前页面句柄
            h = self.driver.current_window_handle
            lists.click()
            # 获取所有句柄
            all_h = self.driver.window_handles
            # 切换句柄
            self.driver.switch_to.window(all_h[1])
            # 关闭新窗口
            self.driver.close()
            # 切换到首页句柄
            self.driver.switch_to.window(h)

    def test_article_01(self):
        lis = self.Article.list_text()
        print(len(lis), "最新资讯")
        self.article_case(lis)

    def test_article_02(self):
        lis = self.Article.list_do()
        print(len(lis), "热点推荐")
        self.article_case(lis)

    def test_article_03(self):
        lis = self.Article.list_a()
        print(len(lis), "本周最热")
        self.article_case(lis)