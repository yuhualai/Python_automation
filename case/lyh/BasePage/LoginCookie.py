#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import time
from case.lyh.BasePage.BasePage import Action


class Cookie(Action):
    def cookie(self):
        self.driver.get("http://www.liangyihui.net/")
        c1 = {'name': 'session',
              'value': 's%3AiOjTCIM4DJisBoWLl09gYnf_luNM8ZT9.u7gTnS67VgXGDjHDv43mONhyFN1OVdWURFIyI6V1eUo'}
        self.driver.add_cookie(c1)
        time.sleep(3)
        self.driver.refresh()
