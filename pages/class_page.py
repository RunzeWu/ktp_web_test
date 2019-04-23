#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 17:19
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : class_page.py
# @Software : PyCharm
from pages.base import BasePage
from pages.locators.class_locator import ClassLocator as cl


class ClassPage(BasePage):

    def click_classmate(self):
        return self.get_visible_element(cl.classmate_locator).click()