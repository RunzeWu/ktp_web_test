#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 17:04
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : classmate_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class ClassmateLocator:

    mouse_needed_move_locator = (By.XPATH, "//li[@class='teacher']")

    message_icon_locator = (By.XPATH, "//a[@class='call']")

    message_input_locator = (By.XPATH, "//*[@id='dvm']//textarea")

    message_submit_locator = (By.XPATH, "//a[@class='btn btn-positive']")

    # //div[@class='text'][contains(.,'雨泽大佬你好帅testbyyysf')]
