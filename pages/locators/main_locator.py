#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 15:50
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : main_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class MainPageLocator:

    joinClass_locator = (By.XPATH, "//div[@class='ktcon1l fl'][contains(.,'加入班级')]")

    inviteCodeInput_locator = (By.XPATH, "//input[@type='text']")

    join_button_locator = (By.XPATH, "//a[contains(.,'加入')]")

    confirm_button_locator = (By.XPATH, "//a[contains(.,'加入')]")

    exit_toast = (By.XPATH, "//span[contains(., '课程退课成功')]")

    exit_locator = (By.XPATH, "//span[contains(.,'UEPLPQ')]/ancestor::dl//a[contains(.,'退课')]")

    code_locator = (By.XPATH, "//*[@id='error-tip']/span")

    class_locator = (By.XPATH, "//a[@data-id='MDAwMDAwMDAwMLOstZeGqbex']")

    icon_locator = (By.XPATH, "//a[contains(@class,'kdmore')]")

    student_locator = (By.XPATH, "//a[contains(.,'同学')]")

    exit_confirm_pwd_input_locator = (By.XPATH, "//input[contains(@type,'password')]")

    exit_confirm_button_locator = (By.XPATH, "//a[@class='btn btn-positive'][contains(.,'退课')]")

    homework_locator = (By.XPATH, "//a[contains(.,'作业1：写两个函数')]")