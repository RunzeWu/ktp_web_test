#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 13:16
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : main_page.py
# @Software : PyCharm
from pages.base import BasePage
from selenium import webdriver
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.locators.main_locator import MainPageLocator as ml
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    邀请码：UEPLPQ
    """

    def click_icon(self):
        return self.get_visible_element(ml.icon_locator).click()

    def click_exit(self):
        return self.get_visible_element(ml.exit_locator).click()

    def input_confirm_pwd(self, pwd):
        return self.get_visible_element(ml.exit_confirm_pwd_input_locator).send_keys(pwd)

    def click_exit_confirm_button(self):
        return self.get_visible_element(ml.exit_confirm_button_locator).click()

    def exit_class(self,pwd):
        self.click_icon()
        self.click_exit()
        self.input_confirm_pwd(pwd)
        self.click_exit_confirm_button()

    def click_join_class(self):
        return self.get_visible_element(ml.joinClass_locator).click()

    def input_verf_code(self,code):
        return self.get_visible_element(ml.inviteCodeInput_locator).send_keys(code)

    def click_jiaru(self):
        return self.get_visible_element(ml.join_button_locator).click()

    def join_class_with_no_class(self, code="UEPLPQ"):
        self.click_join_class()
        self.input_verf_code(code)
        self.click_jiaru()

    def join_class_with_class(self,code):
        self.click_join_class()
        self.input_verf_code(code)
        self.get_visible_element(ml.confirm_button_locator).click()

    def go_into_class(self):
        return self.get_visible_element(ml.class_locator).click()

    def get_toast_text(self, locator):
        return self.get_visible_element(locator).text

    def click_homework(self):
        """
        转到作业页面
        :return:
        """
        return self.get_visible_element(ml.homework_locator).click()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    main_page = MainPage(driver)
    driver.get('https://www.ketangpai.com/')
    index_page.click_login_button()
    login_page.login("17751810779", "wrz19960529.")
    main_page.exit_class("wrz19960529.")
