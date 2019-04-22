#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 11:21
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : index_page.py
# @Software : PyCharm
from pages.base import BasePage
from pages.locators.index_locator import IndexLocator as il
from selenium import webdriver


class IndexPage(BasePage):

    def click_login_button(self):
        return self.get_visible_element(il.login_locator).click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.ketangpai.com/')
    A=IndexPage(driver)
    A.click_login_button()