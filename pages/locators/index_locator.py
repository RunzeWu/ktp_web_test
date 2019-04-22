# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/19 22:26
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :index_locator.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By


class IndexLocator:
    login_locator = (By.XPATH, "//a[contains(@class,'login')]")
