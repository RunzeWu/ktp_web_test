# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/19 22:20
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_locator.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By


class LoginLocators:
    user_locator = (By.XPATH, "//input[contains(@name,'account')]")
    pwd_locator = (By.XPATH, "//input[contains(@type,'password')]")
    submit_locator = (By.XPATH, "//div[@class='padding-cont pt-login']//a[@class='btn-btn']")
