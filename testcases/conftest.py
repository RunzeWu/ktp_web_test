# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/21 22:39
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :conftest.py
# Software  :PyCharm Community Edition
import pytest
from selenium import webdriver
from common.config import ReadConfig


@pytest.fixture(scope="session")
def login():
    driver = webdriver.Chrome()
