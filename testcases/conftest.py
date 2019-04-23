# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/21 22:39
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :conftest.py
# Software  :PyCharm Community Edition
import pytest
from selenium import webdriver
from pages.index_page import IndexPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from common.config import ReadConfig
from datas.login import correct_userInfo
from pages.homework_page import HomeworkPage
from pages.classmate_page import ClassmatePage
from pages.class_page import ClassPage


url = ReadConfig().get_value("web","url")
driver = webdriver.Chrome()
driver.get(url)


@pytest.fixture(scope="session")
def login():
    index_page = IndexPage(driver)
    index_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login(correct_userInfo["account"],correct_userInfo["pwd"])
    # 截至目前进入 main_page
    yield driver

    driver.close()


@pytest.fixture(scope="class")
def join_class_env():
    main_page = MainPage(driver)
    main_page.exit_class(correct_userInfo["pwd"])

    yield main_page

    driver.get("https://www.ketangpai.com/Main/index.html")


@pytest.fixture(scope="class")
def upload_file_env():
    main_page = MainPage(driver)
    main_page.click_homework()
    homework_page = HomeworkPage(driver)

    yield homework_page

    driver.get("https://www.ketangpai.com/Main/index.html")


@pytest.fixture(scope="class")
def send_message():
    main_page = MainPage(driver)
    main_page.go_into_class()
    class_page = ClassPage(driver)
    class_page.click_classmate()
    classmate_page = ClassmatePage(driver)
    yield classmate_page
    driver.get("https://www.ketangpai.com/Main/index.html")


