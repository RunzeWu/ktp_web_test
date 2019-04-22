#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 11:28
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : login_page.py
# @Software : PyCharm
from pages.base import BasePage
from pages.locators.login_locator import LoginLocators as ll
from selenium import webdriver
from pages.index_page import IndexPage


class LoginPage(BasePage):

    def input_account(self, account):
        self.send_keys(ll.user_locator, account)

    def input_pwd(self, pwd):
        self.send_keys(ll.pwd_locator,pwd)

    def click_login_button(self):
        self.get_visible_element(ll.submit_locator).click()

    def login(self,account, pwd):
        self.input_account(account)
        self.input_pwd(pwd)
        self.click_login_button()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.ketangpai.com/')
    B = IndexPage(driver)
    A=LoginPage(driver)
    B.click_login_button()
    A.login("17751810779","wrz19960529.")