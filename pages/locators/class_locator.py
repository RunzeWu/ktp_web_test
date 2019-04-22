#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 17:17
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : class_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class ClassLocator:

    classmate_locator = (By.XPATH, "//a[contains(.,'同学')]")