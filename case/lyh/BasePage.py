#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def browser(browser='firefox'):
    try:
        if browser == 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can enter 'firefox', 'chrome', 'ie', or 'phantomjs'")
    except Exception as msg:
        print("%s" % msg)


class Action:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url, t='', timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Erroe:%s" % msg)

    # 定位元素方法封装，参数locator是元祖类型
    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    # 定位一组元素
    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def texts(self, locator, i):
        elements = self.find_elements(locator)[i].text
        return elements

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # 判断文本在元素里，没定位到元素返回False，定位到单号判断结果布尔值
    def is_text_in_element(self, locator, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            print(result)
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    # 判断元素的value的值，没定位到元素返回false，定位到返回判断结果布尔值
    def is_text_in_value(self, locator, value, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    # 判断title完全等于
    def is_title(self, title, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    # 判断title包含
    def is_title_contain(self, title, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    # 判断元素被选中，返回布尔值
    def is_selected(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    # 判断元素的状态，selected是期望的参数true/False 返回布尔值
    def is_selected_be(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(locator))
        return result

    # 判断页面是否有alert
    def is_alert_present(self, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    # 元素可见返回本身，不可见返回False
    def is_visbility(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        return result

    # 元素可见返回本身，不可见返回True,没有找到元素返回True
    def is_invisbility(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(locator))
        return result

    # 元素可以点击is_enabled返回本身，不可点击返回False
    def is_clickable(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    # 判断元素有没被定为到（并意味着可见），定为到返回element，没定位到返回False
    def is_located(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    # 鼠标悬停操作
    def move_to_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # 返回操作
    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取文本
    def get_text(self, locator):
        element = self.find_element(locator).text
        return element

    # 获取属性
    def get_attribute(self, locator, name):
        element = self.find_element(locator)
        return element.get_attribute(name)

    # 执行js
    def js_execute(self, js):
        return self.driver.execute_script(js)

    # 聚焦元素
    def js_focue_element(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 滚动到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    # 滚动到底部
    def js_scroll_end(self):
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 通过索引，index是索引第几个，从0开始
    def select_by_index(self, locator, index):
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    # 通过value属性
    def select_by_value(self, locator, value):
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    # 通过文本值定位
    def select_by_text(self, locator, text):
        element = self.find_element(locator)
        Select(element).select_by_value(text)

    # 获取句柄
    def window_handles(self, i):
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[i])
