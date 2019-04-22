# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 17:30
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By

inviteCode_correct = [{"code": "UEPLPQ","locator":(By.XPATH, "//span[contains(., '加入课堂成功')]")}]

inviteCode_incorrect = [{"code": "UEPLPQ","expected":"你已经选过此课程","locator":(By.XPATH, "//span[contains(., '你已经选过此课程')]")},
                        {"code": "asasas","expected":"不存在","locator":(By.XPATH, "//span[contains(., '不存在')]")}]

